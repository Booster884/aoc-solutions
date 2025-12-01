parseLine :: String -> Int
parseLine (x : xs)
  | x == 'L' = -read xs
  | x == 'R' = read xs

main = do
  -- numbers <- map parseLine . lines <$> return "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
  numbers <- map parseLine . lines <$> readFile "input"
  print $ length $ filter (== 0) $ scanl (\a b -> mod (a + b) 100) 50 numbers
  print $ snd $ foldl (\(a, c) b -> (mod (a + b) 100, c + abs (div (a + b) 100))) (50, 0) numbers
