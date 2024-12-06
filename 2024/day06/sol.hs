import Data.HashSet (HashSet, fromList)
import qualified Data.HashSet as HashSet
import Data.List (transpose)

type Point = (Int, Int)
type GridState = (HashSet Point, Point, Point, Point, HashSet Point, HashSet (Point, Point))

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
                 HashSet.empty,
                 HashSet.empty)

rotate :: Point -> Point
rotate (-1, 0) = (0, -1)
rotate (0, -1) = (1, 0)
rotate (1, 0) = (0, 1)
rotate (0, 1) = (-1, 0)

move :: GridState -> (HashSet Point, Bool)
move (obs, (w, h), (x, y), (dx, dy), been, dirBeen)
    | obstructed = move (obs, (w, h), (x, y), rotate (dx, dy), newBeen, newDirBeen)
    | outOfBounds = (newBeen, False)
    | loop = (newBeen, True)
    | otherwise = move (obs, (w, h), (nx, ny), (dx, dy), newBeen, newDirBeen)
    where (nx, ny) = (x + dx, y + dy)
          obstructed = HashSet.member (nx, ny) obs
          outOfBounds = not (nx > 0 && nx < w && ny > 0 && ny < w)
          loop = HashSet.member ((x, y), (dx, dy)) dirBeen
          newBeen = HashSet.insert (x, y) been
          newDirBeen = HashSet.insert ((x, y), (dx, dy)) dirBeen

solve2 :: GridState -> HashSet Point -> Int
solve2 (obs, size, pos, dir, _, _) been = length $ filter snd $
    [move (HashSet.insert x obs, size, pos, dir, HashSet.empty, HashSet.empty)
     | x <- HashSet.toList been, x /= pos]

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let startState = newState $ transpose inLines
       let (been, False) = move startState
       print $ HashSet.size been
       print $ solve2 startState been
