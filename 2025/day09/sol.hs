-- I recommend compiling with -O2, this should cut the running time down to < 0.3s.
import Data.Char (isDigit)
import Text.ParserCombinators.ReadP

type Point = (Int, Int)

type Edge = (Point, Point)

intP :: ReadP Int
intP = read <$> many1 (satisfy isDigit)

pointP :: ReadP Point
pointP = (,) <$> intP <*> (char ',' *> intP)

parse :: ReadP [Point]
parse = (sepBy pointP $ char '\n')

area (x0, y0) (x1, y1) = (abs (x1 - x0) + 1) * (abs (y1 - y0) + 1)

part1 :: [Point] -> Int
part1 points = maximum [area a b | a <- points, b <- points, a < b]

path :: [Point] -> [Edge]
path points = take (length points) $ zip pointsCycle (tail pointsCycle)
  where
    pointsCycle = cycle points

norm :: (Point, Point) -> (Point, Point)
norm ((x0, y0), (x1, y1)) = ((min x0 x1, min y0 y1), (max x0 x1, max y0 y1))

rectLineIntersect :: (Point, Point) -> Edge -> Bool
rectLineIntersect rect line =
  if lx0 == lx1
    then lx0 > rx0 && lx0 < rx1 && ly0 < ry1 && ly1 > ry0
    else ly0 > ry0 && ly0 < ry1 && lx0 < rx1 && lx1 > rx0
  where
    ((rx0, ry0), (rx1, ry1)) = norm rect
    ((lx0, ly0), (lx1, ly1)) = norm line

part2 points =
  let edges = path points
      valid a b = all (not . rectLineIntersect (a, b)) edges
   in maximum [area a b | a <- points, b <- points, a < b, valid a b]

main = do
  points <- fst . last . readP_to_S parse <$> readFile "input"
  testPoints <- fst . last . readP_to_S parse <$> readFile "test"

  -- print $ part1 testPoints
  -- print $ part2 testPoints

  print $ part1 points
  print $ part2 points
