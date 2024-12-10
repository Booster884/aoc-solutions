import Data.List (singleton)
import qualified Data.Set as Set

type Point = (Int, Int)
type Grid = ([[Int]], (Int, Int))

neighborhood = [(0,1), (1, 0), (0, -1), (-1, 0)]

gridSize grid = (length $ head grid, length grid)

charAtPos :: [[Int]] -> Point -> Int
charAtPos grid (x, y) = grid !! y !! x

inBounds :: (Int, Int) -> Point -> Bool
inBounds (w, h) (x, y) = x >= 0 && x < w && y >= 0 && y < h

movableNeigbors :: Grid -> Point -> [Point]
movableNeigbors (grid, (w, h)) (x, y) =
    filter (\newPos -> charAtPos grid newPos == charAtPos grid (x, y) + 1)
    $ filter (inBounds (w, h)) newPoss
    where newPoss = [(x + dx, y + dy) | (dx, dy) <- dirs]
          dirs = neighborhood

trailheads :: Grid -> [Point]
trailheads (grid, (w, h)) = [(x, y) | x <- [0..w-1], y <- [0..h-1], charAtPos grid (x, y) == 0]

peaksFromHere :: Grid -> Point -> [Point]
peaksFromHere g@(grid, (w, h)) pos
    | charAtPos grid pos == 9 = singleton pos
    | null moves = []
    | otherwise = concatMap (peaksFromHere g) moves
    where moves = movableNeigbors g pos

solve1 :: Grid -> Int
solve1 g = sum . map (length . Set.fromList . peaksFromHere g) $ trailheads g

solve2 :: Grid -> Int
solve2 g = sum . map (length . peaksFromHere g) $ trailheads g

main :: IO ()
main =
    do grid' <- map (map (read . singleton)) . lines <$> readFile "test"
       let grid = (grid', gridSize grid')
       print $ solve1 grid
       print $ solve2 grid
