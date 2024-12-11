import Data.List (splitAt, partition)
import Data.Function (on)
import Data.Ratio ((%))
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map

data BlinkRes = Only Int | Both Int Int
    deriving (Show)
type IntOccur = Map Int Int

mapPair f = uncurry ((,) `on` f)

evenDigitCount :: Int -> Bool
evenDigitCount x = even $ length $ show x

splitDigits :: Int -> (Int, Int)
splitDigits x = mapPair read $ splitAt (floor (length w % 2)) w
    where w = show x

singleIter :: Int -> BlinkRes
singleIter x | x == 0 = Only 1
             | evenDigitCount x = let (a, b) = splitDigits x in Both a b
             | otherwise = Only (x * 2024)

addIter :: Int -> Int -> IntOccur -> IntOccur
addIter n x xs = case singleIter x of
    Only y -> Map.insertWith (+) y n xs
    Both a b -> Map.insertWith (+) a n $ Map.insertWith (+) b n xs

iter :: IntOccur -> IntOccur
iter = Map.foldrWithKey (flip addIter) Map.empty

solve :: Int -> IntOccur -> Int
solve n = sum . map snd . Map.toList . last . take (n+1) . iterate iter

main :: IO ()
main =
    do numbers :: [Int] <- map read . words <$> readFile "test"
       let numOccur :: IntOccur = Map.fromList $ map (, 1) numbers
       print $ solve 25 numOccur
       print $ solve 75 numOccur
