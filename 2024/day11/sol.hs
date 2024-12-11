{-# LANGUAGE TupleSections #-}
import Data.List (splitAt, partition)
import Data.Function (on)
import Data.Ratio ((%))

type IntOccur = (Int, Int)

mapPair f = uncurry ((,) `on` f)

evenDigitCount :: Int -> Bool
evenDigitCount x = even $ length $ show x

splitDigits :: Int -> (Int, Int)
splitDigits x = mapPair read $ splitAt (floor (length w % 2)) w
    where w = show x

iter :: [IntOccur] -> [IntOccur]
iter ((x, n):xs) | x == 0 = (1, n) : iter xs
                 | evenDigitCount x = let (a, b) = splitDigits x in (a, n) : (b, n) : iter xs
                 | otherwise = (x * 2024, n) : iter xs
iter [] = []

simplify :: [IntOccur] -> [IntOccur]
simplify ((x, n):xs) = (x, n + sum (map snd sameVal)) : simplify otherVal
    where (sameVal, otherVal) = partition (\y -> x == fst y) xs
simplify [] = []

solve :: Int -> [IntOccur] -> Int
solve n = sum . map snd . last . take (n+1) . iterate (simplify . iter)

main :: IO ()
main =
    do numbers :: [Int] <- map read . words <$> readFile "input"
       let numOccur = map (, 1) numbers
       print $ solve 25 numOccur
       print $ solve 75 numOccur
