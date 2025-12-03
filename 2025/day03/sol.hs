import Data.List (maximumBy)
import Data.Ord (comparing)

testInput = "987654321111111\n811111111111119\n234234234234278\n818181911112111"

dropBack n xs = take (length xs - n) xs

maxDigits :: Int -> [Int] -> [Int]
maxDigits 0 _ = []
maxDigits n xs = y : maxDigits (n - 1) ys
  where
    (y, ys) = maximumBy cmp . headTailsN (n - 1) $ xs
    cmp = comparing fst <> comparing (length . snd)

-- | All combinations of heads and tails, where the tails are at least length 'n'.
headTailsN n (x : xs)
  | length xs >= n = (x, xs) : headTailsN n xs
  | otherwise = []
headTailsN _ [] = []

undigits :: [Int] -> Int
undigits = foldl (\acc x -> acc * 10 + x) 0

main = do
  let (f :: String -> [[Int]]) = map (map (read . (: []))) . lines
  -- a <- f <$> return testInput
  a <- f <$> readFile "input"
  print $ sum $ map (undigits . maxDigits 2) a
  print $ sum $ map (undigits . maxDigits 12) a
