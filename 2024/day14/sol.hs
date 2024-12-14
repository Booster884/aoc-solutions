import Text.ParserCombinators.ReadP
import Data.Char (isNumber)

type Point = (Int, Int)

number :: ReadP Int
number = do
    sign <- option ' ' $ char '-'
    num <- many1 $ satisfy isNumber
    return $ read (sign:num)

pointP :: ReadP Point
pointP = do
    x <- number
    char ','
    y <- number
    return (x, y)

entryP :: ReadP (Point, Point)
entryP = do
    string "p="
    pos <- pointP
    string " v="
    vel <- pointP
    char '\n'
    return (pos, vel)

move :: (Int, Int) -> (Point, Point) -> (Point, Point)
move (w, h) ((x, y), v@(dx, dy)) = (((x + dx + w) `mod` w, (y + dy + h) `mod` h), v)

moveAll :: (Int, Int) -> [(Point, Point)] -> [(Point, Point)]
moveAll (w, h) = map (move (w, h))

quadrants :: (Int, Int) -> [Point] -> [Int]
quadrants (w, h) ps = map (\f -> length $ filter f ps) inQuads
    where inQuads = [ \(x, y) -> x < mx && y < my
                    , \(x, y) -> x < mx && y > my
                    , \(x, y) -> x > mx && y < my
                    , \(x, y) -> x > mx && y > my
                    ]
          mx = w `div` 2
          my = h `div` 2

solve1 :: (Int, Int) -> Int -> [(Point, Point)] -> Int
solve1 bounds n entries = product $ quadrants bounds $ map fst
    $ last $ take (n + 1) $ iterate (moveAll bounds) entries

displayRobots :: (Int, Int) -> Int -> [Point] -> String
displayRobots (w, h) i ps = show i ++ '\n' : unlines [[int2char $ length $ filter (== (x, y)) ps | x <- [0..w-1]] | y <- [0..h-1]]
    where int2char 0 = '.'
          int2char _ = '#'

solve2 :: (Int, Int) -> [(Point, Point)] -> String
solve2 bounds entries = concatMap (uncurry $ displayRobots bounds) lowEntropySteps
    where steps :: [(Int, [Point])] = zip [0..] $ map (map fst) $ take 10000 $ iterate (moveAll bounds) entries
          lowEntropySteps = filter (\(_, ps) -> any (40 >) $ quadrants bounds ps) steps

main :: IO ()
main =
    do let filename = "input"
       entries <- fst . last . readP_to_S (many entryP) <$> readFile filename
       let bounds = if filename == "test" then (11, 7) else (101, 103)
       print $ solve1 bounds 100 entries
       putStr $ solve2 bounds entries
       -- Now manually find the tree in the output
