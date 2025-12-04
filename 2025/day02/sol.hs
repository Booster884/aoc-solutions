import Data.Char (isDigit)
import Data.List (nub, (\\))
import Data.Maybe (fromMaybe)
import Text.ParserCombinators.ReadP

testInput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

intP :: ReadP Int
intP = read <$> many1 (satisfy isDigit)

rangeP :: ReadP (Int, Int)
rangeP = (,) <$> intP <*> (char '-' *> intP)

parse :: ReadP [(Int, Int)]
parse = sepBy rangeP (char ',')

digits :: Int -> Int
digits = length . show

rep n x = f n (digits x) * x
  where
    f 1 ls = 1
    f n ls = 10 ^ ls * f (n - 1) ls + 1

prefix' n x = 10 ^ (digits p)
  where
    l = digits x
    ls = l `div` n
    p = (x `div` 10 ^ (l - ls))

prefix n x | l `mod` n == 0 = Just (x `div` 10 ^ (l - ls))
  where
    l = digits x
    ls = l `div` n
prefix _ _ = Nothing

invalidInRange n (start, end) =
  filter (>= start) $
    takeWhile (<= end) $
      map (rep n) [(fromMaybe (prefix' n start) $ prefix n start) ..]

splitRange :: (Int, Int) -> [(Int, Int)]
splitRange r@(start, end)
  | digits start == digits end = [r]
  | digits start - digits end == -1 = [(start, x - 1), (x, end)]
  where
    x = 10 ^ (digits start)

main = do
  ranges <- concatMap splitRange . fst . last . readP_to_S parse <$> readFile "input"

  print $ sum $ concat $ map (invalidInRange 2) ranges
  print $ sum $ nub $ concat $ concatMap (\r@(s, _) -> [invalidInRange n r | n <- [2 .. digits s]]) ranges
