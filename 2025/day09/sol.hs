import Data.Char (isDigit)
import Data.List (sortBy)
import Data.Ord (Down (..), comparing)
import Text.ParserCombinators.ReadP

type Point = (Int, Int)

intP :: ReadP Int
intP = read <$> many1 (satisfy isDigit)

pointP :: ReadP Point
pointP = (,) <$> intP <*> (char ',' *> intP)

parse :: ReadP [Point]
parse = (sepBy pointP $ char '\n')

area (x0, y0) (x1, y1) = (abs (x1 - x0) + 1) * (abs (y1 - y0) + 1)

part1 :: [Point] -> Int
part1 points = head $ sortBy (comparing Down) [area a b | a <- points, b <- points, a < b]

main = do
  points <- fst . last . readP_to_S parse <$> readFile "input"
  testPoints <- fst . last . readP_to_S parse <$> readFile "test"

  print $ part1 testPoints
  print $ part1 points
