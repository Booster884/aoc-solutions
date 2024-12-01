import Data.List (sort)
import Data.Function (on)

each :: [String] -> (Int, Int)
each line = (head a, last a)
    where a = map read line

-- Stolen from StackOverflow :(((
mapPair f = uncurry ((,) `on` f)

sortedPairs :: [String] -> ([Int], [Int])
sortedPairs = mapPair sort . unzip . map (each . words)

solve1 aa = sum . map (abs . uncurry (-)) . uncurry zip $ sortedPairs aa

count x = length . filter (x==)

solve2 :: [Int] -> [Int] -> Int
solve2 a b = sum $ map (\x -> count x b * x) a

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       print $ solve1 inLines
       print $ uncurry solve2 $ sortedPairs inLines
