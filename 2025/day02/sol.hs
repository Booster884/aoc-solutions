import Data.Char (isDigit)
import Debug.Trace (trace)
import Text.ParserCombinators.ReadP

testInput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

intP :: ReadP Int
intP = read <$> many1 (satisfy isDigit)

-- Something like `rangeP = (,) <$> intP <* char '-' *> intP` might be better?
rangeP :: ReadP (Int, Int)
rangeP = do
  a <- intP
  char '-'
  b <- intP
  return (a, b)

parse :: ReadP [(Int, Int)]
parse = sepBy rangeP (char ',')

-- | Check if a string is made of 'n' repetitions of the same substring.
hasNRepeats :: Int -> String -> Bool
hasNRepeats n xs
  | length xs `mod` n == 0 = f l (take l xs) (drop l xs)
  | otherwise = False
  where
    l = (length xs `div` n)
    f _ ts [] = True
    f l ts xs = ts == take l xs && f l ts (drop l xs)

hasAnyRepeats :: String -> Bool
hasAnyRepeats xs = any id [hasNRepeats n xs | n <- [2 .. l]]
  where
    l = length xs

main = do
  -- a <- fst . last . readP_to_S parse <$> return testInput
  a <- fst . last . readP_to_S parse <$> readFile "input"
  print $ sum $ foldl (++) [] $ map (\(a, b) -> filter (hasNRepeats 2 . show) [a .. b]) a
  print $ sum $ foldl (++) [] $ map (\(a, b) -> filter (hasAnyRepeats . show) [a .. b]) a

