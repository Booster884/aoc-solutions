{-# LANGUAGE OverloadedStrings #-}
import qualified Data.Text as T

type Lengths = [Int]
data Entry = Lock Lengths | Key Lengths
    deriving (Show)

isLock (Lock _) = True
isLock (Key _) = False

parseEntry :: [T.Text] -> Entry
parseEntry xs = if key then Key lengths else Lock lengths
    where lengths = map ((\x -> x - 1) . T.length . (if key then last else head) . T.group) xs
          key = '.' == T.head (head xs)

fits :: Entry -> Entry -> Bool
fits (Lock lensL) (Key lensK) = all (<= 5) $ zipWith (+) lensL lensK
fits _ _ = error "Every lock needs a key, and only in that order."

main :: IO ()
main =
    do entries <- map (parseEntry . T.transpose . T.splitOn "\n")
                  . T.splitOn "\n\n"
                  . T.pack <$> readFile "input"
       let locks = filter isLock entries
       let keys = filter (not . isLock) entries
       print $ length [(l, k) | l <- locks, k <- keys, fits l k]
