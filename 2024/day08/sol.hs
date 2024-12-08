import qualified Data.Set as Set
import Data.Set (Set)
import Data.Ratio ((%))

type Point = (Int, Int)
type Antennas = [[Point]]

size :: [String] -> (Int, Int)
size grid = (length $ head grid, length grid)

antennas :: [String] -> Antennas
antennas grid = map (\c -> [(x, y) | x <- [0..w-1], y <- [0..h-1], grid !! y !! x == c])
    $ Set.toList chars
    where (w, h) = size grid
          chars = Set.filter (/= '.') $ Set.fromList $ concat grid

antinodePair :: (Point, Point) -> [Point]
antinodePair ((x0, y0), (x1, y1)) = [(x0 - dx, y0 - dy), (x1 + dx, y1 + dy)]
    where (dx, dy) = (x1 - x0, y1 - y0)

antinodes :: [Point] -> Set Point
antinodes ps = Set.fromList $ concatMap antinodePair $ [(a, b) | a <- ps, b <- ps, a /= b]

solve1 :: (Int, Int) -> Antennas -> Set Point
solve1 (w, h) as = Set.filter (\(x, y) -> x >= 0 && x < w && y >= 0 && y < h)
    $ foldr (Set.union . antinodes) Set.empty as

inLineWith :: (Point, Point) -> Point -> Bool
inLineWith ((x0, y0), (x1, y1)) (x, y)
    | (x, y) `elem` [(x0, y0), (x1, y1)] = True
    | x `elem` [x0, x1] || y `elem` [y0, y1] = False
    | otherwise = (y1 - y0) % (x1 - x0) == (y - y0) % (x - x0)

inLineWithAny :: Antennas -> Point -> Bool
inLineWithAny as point = any (\ps -> any (`inLineWith` point) [(a, b) | a <- ps, b <- ps, a /= b]) as

solve2 (w, h) as = filter (as `inLineWithAny`) points
    where points = [(x, y) | x <- [0..w-1], y <- [0..h-1]]

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let gridSize = size inLines
       print $ length $ solve1 gridSize $ antennas inLines
       print $ length $ solve2 gridSize $ antennas inLines
