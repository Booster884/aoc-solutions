import qualified Data.Map as Map
import Data.Map (Map)
import qualified Data.Set as Set
import Data.Set (Set)
import Data.Ratio ((%))

type Point = (Int, Int)
type Antennas = [(Char, [Point])]

pairs :: [a] -> [(a, a)]
pairs xs = zip (tail xs) xs

size :: [String] -> (Int, Int)
size grid = (length $ head grid, length grid)

antennas :: [String] -> Antennas
antennas grid = map (\c -> (c, [(x, y) | x <- [0..w-1], y <- [0..h-1], grid !! y !! x == c]))
    $ Set.toList chars
    where (w, h) = size grid
          chars = Set.filter (/= '.') $ Set.fromList $ concat grid

antipodePair :: (Point, Point) -> [Point]
antipodePair ((x0, y0), (x1, y1)) = [(x0 - dx, y0 - dy), (x1 + dx, y1 + dy)]
    where (dx, dy) = (x1 - x0, y1 - y0)

antipodes :: [Point] -> Set Point
antipodes ps = Set.fromList $ concatMap antipodePair $ [(x, y) | x <- ps, y <- ps, x /= y]

solve1 :: (Int, Int) -> Antennas -> Set Point
solve1 (w, h) as = Set.filter (\(x, y) -> x >= 0 && x < w && y >= 0 && y < h)
    $ foldr (Set.union . (\(_, xs) -> antipodes xs)) Set.empty as

inLineWith :: (Point, Point) -> Point -> Bool
inLineWith ((x0, y0), (x1, y1)) (x, y)
    | (x, y) `elem` [(x0, y0), (x1, y1)] = True
    | x `elem` [x0, x1] || y `elem` [y0, y1] = False
    | otherwise = (y1 - y0) % (x1 - x0) == (y - y0) % (x - x0)

inLineWithAny :: [Point] -> Point -> Bool
inLineWithAny ps point = any (`inLineWith` point) [(x, y) | x <- ps, y <- ps, x /= y]

inLineWithAny' :: Antennas -> Point -> Bool
inLineWithAny' as point = any ((`inLineWithAny` point) . snd)  as

solve2 (w, h) as = filter (as `inLineWithAny'`) points
    where points = [(x, y) | x <- [0..w-1], y <- [0..h-1]]

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let gridSize = size inLines
       print $ length $ solve1 gridSize $ antennas inLines
       print $ length $ solve2 gridSize $ antennas inLines

