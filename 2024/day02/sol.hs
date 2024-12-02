sign :: Int -> Int
sign x | x < 0 = -1
       | x == 0 = 0
       | x > 0 = 1

safe :: [Int] -> Bool
safe xs = all (head signs ==) (tail signs) && all ((`elem` [1..3]) . abs) diffs
    where
        pairs xs = zip (tail xs) xs
        diffs = map (uncurry (-)) $ pairs xs
        signs = map sign diffs

solve1 :: [[Int]] -> Int
solve1 = length . filter safe

solve2 = undefined

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let reports = map (map read . words) inLines
       print $ solve1 reports
       -- print $ solve2 reports
