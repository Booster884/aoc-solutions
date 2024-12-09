import Data.List (dropWhileEnd)

type Id = Int
data Frag = Empty | File Int
    deriving (Eq)

instance Show Frag where
    show (File x) = show x
    show Empty = "."

parseLine :: Int -> [Char] -> [Frag]
parseLine n (f:e:xs) = replicate (read [f]) (File n) ++ replicate (read [e]) Empty ++ parseLine (n + 1) xs
parseLine n [f] = replicate (read [f]) (File n)

defrag :: [Frag] -> [Frag]
defrag (File n:xs) = File n : defrag xs
defrag (Empty:xs) = if null xs then [] else
    let sxs = dropWhileEnd (== Empty) xs in last sxs : defrag (init sxs)
defrag _ = []

checksum :: [Frag] -> Int
checksum = sum . zipWith (\i (File n) -> n * i) [0..]

solve1 = undefined

solve2 = undefined

main :: IO ()
main =
    do inLine <- init <$> readFile "test"
       let blocks = parseLine 0 inLine
       print $ checksum $ defrag blocks
       -- print $ defrag blocks
       -- print $ solve2 inLines
