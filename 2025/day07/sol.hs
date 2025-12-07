rotate :: Int -> [a] -> [a]
rotate n xs = take l . drop (n `mod` l) . cycle $ xs
  where
    l = length xs

countSplits :: ([Bool], Int) -> String -> ([Bool], Int)
countSplits (t, n) r = (t', n + foldr (\x acc -> if x then acc + 1 else acc) 0 hits)
  where hits = zipWith (\a b -> b == '^' && a) t r
        misses = zipWith (\a b -> b /= '^' && a) t r
        t' = zipWith3 (\a b c -> a || b || c) misses (rotate 1 hits) (rotate (-1) hits)

multiverse :: [Int] -> String -> [Int]
multiverse t r = t'
  where hits = zipWith (\a b -> if b == '^' then a else 0) t r
        misses = zipWith (\a b -> if b /= '^' then a else 0) t r
        t' = zipWith3 (\a b c -> a + b + c) misses (rotate 1 hits) (rotate (-1) hits)

boolToInt False = 0
boolToInt True = 1

main = do
  -- a <- filter (not . all (== '.')) . lines <$> readFile "test"
  a <- filter (not . all (== '.')) . lines <$> readFile "input"

  let t = map (== 'S') $ head a

  print $ snd $ foldl (countSplits) (t, 0) a
  print $ foldl (+) 0 $ foldl multiverse (map boolToInt t) a
