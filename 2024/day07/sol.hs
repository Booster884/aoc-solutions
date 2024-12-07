parseLine :: String -> (Int, [Int])
parseLine line = (read $ init x, map read xs)
    where x:xs = words line

valid :: (Int, [Int]) -> Bool
valid (res, [x]) = res == x
valid (res, x:y:xs) = valid (res, x+y:xs) || valid (res, x*y:xs)

concatInt :: Int -> Int -> Int
concatInt x y = read (show x ++ show y)

valid' :: (Int, [Int]) -> Bool
valid' (res, [x]) = res == x
valid' (res, x:y:xs) = valid' (res, x+y:xs) || valid' (res, x*y:xs) || valid' (res, x`concatInt`y:xs)

solve f = sum . map fst . filter f . map parseLine

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       print $ solve valid inLines
       print $ solve valid' inLines
