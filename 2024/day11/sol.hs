import Data.List (splitAt)
import Data.Function (on)
import Data.Ratio ((%))

mapPair f = uncurry ((,) `on` f)

evenDigitCount :: Int -> Bool
evenDigitCount x = even $ length $ show x

splitDigits :: Int -> (Int, Int)
splitDigits x = mapPair read $ splitAt (floor (length w % 2)) w
    where w = show x

iter :: [Int] -> [Int]
iter (x:xs) | x == 0 = 1 : iter xs
            | evenDigitCount x = let (a, b) = splitDigits x in a : b : iter xs
            | otherwise = x * 2024 : iter xs
iter [] = []

solve :: Int -> [Int] -> Int
solve n = length . last . take (n+1) . iterate iter

main :: IO ()
main =
    do numbers :: [Int] <- map read . words <$> readFile "input"
       print $ solve 25 numbers
       -- print $ solve 75 numbers
