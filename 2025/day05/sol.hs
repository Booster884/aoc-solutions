import Data.Char (isDigit)
import Data.List (sortBy)
import Text.ParserCombinators.ReadP

testInput = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"

intP :: ReadP Int
intP = read <$> many1 (satisfy isDigit)

rangeP :: ReadP (Int, Int)
rangeP = (,) <$> intP <*> (char '-' *> intP)

rangesP :: ReadP [(Int, Int)]
rangesP = sepBy rangeP $ char '\n'

parse :: ReadP ([(Int, Int)], [Int])
parse = (,) <$> rangesP <*> (string "\n\n" *> (sepBy intP $ char '\n'))

-- Assumes ranges are sorted such that the first range begins before the second one.
overlap (_, a) (b, _) = a >= b

merge (x : r : rs)
  | overlap x r = merge $ (fst x, max (snd x) (snd r)) : rs
  | otherwise = x : merge (r : rs)
merge [x] = [x]
merge [] = []

-- fixG rs = if rs == rs' then rs else fixG rs'
--   where rs' = foldr g [] $ sortBy (\a b -> compare (fst a) (fst b)) rs

main = do
  -- (ranges, ingredients) <- fst . last . readP_to_S parse <$> return testInput
  (ranges, ingredients) <- fst . last . readP_to_S parse <$> readFile "input"

  print $ length $ filter (\ing -> any (\(lower, upper) -> ing >= lower && ing <= upper) ranges) ingredients
  print $ sum $ map (\(a, b) -> b - a + 1) $ merge $ sortBy (\a b -> compare (fst a) (fst b)) ranges
