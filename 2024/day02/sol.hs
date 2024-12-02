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

dampened :: [a] -> [[a]]
dampened xs = [take i xs ++ drop (i + 1) xs | i <- [0..length xs - 1]]
    where l = length xs

anySafe :: [Int] -> Bool
anySafe xs | safe xs = True
           | otherwise = any safe $ dampened xs

solve2 :: [[Int]] -> Int
solve2 = length . filter anySafe

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       let reports = map (map read . words) inLines
       print $ solve1 reports
       print $ solve2 reports
