import Data.Set (Set, fromList)
import qualified Data.Set as Set
import Data.List (transpose)

type Point = (Int, Int)
type GridState = (Set Point, Point, Point, Point, Set Point)

findPosOf :: Char -> [String] -> [(Int, Int)]
findPosOf char grid = [(i, j) | i <- [0..length grid - 1], j <- [0..length (head grid) - 1], grid !! i !! j == char]

obstructions :: [String] -> [(Int, Int)]
obstructions = findPosOf '#'

guardPos :: [String] -> (Int, Int)
guardPos = head . findPosOf '^'

newState :: [String] -> GridState
newState grid = (fromList $ obstructions grid,
                 (length grid -1 ,length (head grid) - 1),
                 guardPos grid,
                 (0, -1),
                 Set.empty)

rotate :: Point -> Point
rotate (-1, 0) = (0, -1)
rotate (0, -1) = (1, 0)
rotate (1, 0) = (0, 1)
rotate (0, 1) = (-1, 0)

move :: GridState -> GridState
move (obs, (w, h), (x, y), (dx, dy), been)
    | obstructed = move (obs, (w, h), (x, y), rotate (dx, dy), newBeen)
    | outOfBounds = (obs, (w, h), (x, y), (dx, dy), newBeen)
    | otherwise = move (obs, (w, h), (nx, ny), (dx, dy), newBeen)
    where (nx, ny) = (x + dx, y + dy)
          obstructed = Set.member (nx, ny) obs
          outOfBounds = not (nx `elem` [0..w] && ny `elem` [0..h])
          newBeen = Set.insert (x, y) been

solve1 :: GridState -> Int
solve1 gs = Set.size been
    where (_, _, _, _, been) = move gs

solve2 = undefined

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let startState = newState $ transpose inLines
       print $ solve1 startState
       -- 5238 too low
       -- print $ solve2 inLines
