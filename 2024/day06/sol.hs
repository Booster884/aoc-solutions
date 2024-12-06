import Data.Set (Set, fromList)
import qualified Data.Set as Set
import Data.List (transpose)

type Point = (Int, Int)
type GridState = (Set Point, Point, Point, Point, Set Point, Set (Point, Point))

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
                 Set.empty,
                 Set.empty)

rotate :: Point -> Point
rotate (-1, 0) = (0, -1)
rotate (0, -1) = (1, 0)
rotate (1, 0) = (0, 1)
rotate (0, 1) = (-1, 0)

move :: GridState -> (Set Point, Bool)
move (obs, (w, h), (x, y), (dx, dy), been, dirBeen)
    | obstructed = move (obs, (w, h), (x, y), rotate (dx, dy), newBeen, newDirBeen)
    | outOfBounds = (newBeen, False)
    | loop = (newBeen, True)
    | otherwise = move (obs, (w, h), (nx, ny), (dx, dy), newBeen, newDirBeen)
    where (nx, ny) = (x + dx, y + dy)
          obstructed = Set.member (nx, ny) obs
          outOfBounds = not (nx `elem` [0..w] && ny `elem` [0..h])
          loop = Set.member ((x, y), (dx, dy)) dirBeen
          newBeen = Set.insert (x, y) been
          newDirBeen = Set.insert ((x, y), (dx, dy)) dirBeen

-- Slow as hell
solve2 :: GridState -> Set Point -> Int
solve2 (obs, size, pos, dir, _, _) been = length $ filter snd $
    [move (Set.insert x obs, size, pos, dir, Set.empty, Set.empty)
     | x <- Set.toList been, x /= pos]

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let startState = newState $ transpose inLines
       let (been, False) = move startState
       print $ Set.size been
       print $ solve2 startState been
