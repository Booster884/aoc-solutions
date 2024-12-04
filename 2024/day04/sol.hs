import Data.List (isPrefixOf, transpose)

occurrences' :: (Eq a) => (Int, [a]) -> [a] -> (Int, [a])
occurrences' (n, s@(_:xs)) needle = if needle `isPrefixOf` s
    then occurrences' (n+1, xs) needle
    else occurrences' (n, xs) needle
occurrences' (n, []) needle = (n, [])


occurrences :: (Eq a) => [a] -> [a] -> Int
occurrences needle haystack = fst $ occurrences' (0, haystack) needle

biDirOcc needle haystack = occurrences needle haystack
    + occurrences needle (reverse haystack)

diagonalise :: [[Char]] -> [[Char]]
diagonalise grid = transpose $ [replicate i ' ' ++ (grid !! i) | i <- [0..length grid - 1]]

solve1 grid = sum (map (biDirOcc "XMAS") grid)
    + sum (map (biDirOcc "XMAS") $ transpose  grid)
    + sum (map (biDirOcc "XMAS") $ diagonalise $ reverse grid)
    + sum (map (biDirOcc "XMAS") $ diagonalise grid)
    where diag = diagonalise grid


findAs :: [[Char]] -> [(Int, Int)]
findAs grid = [(i, j) | i <- [1..length grid - 2], j <- [1..length (head grid) - 2], grid !! i !! j == 'A']

xmasAtPos :: [[Char]] -> (Int, Int) -> Bool
xmasAtPos grid (i, j) = map (\(di, dj) -> grid !! (i + di) !! (j + dj)) offsets `elem` possible
    where offsets = [(di, dj) | di <- [-1, 1], dj <- [-1, 1]]
          possible = ["MMSS", "SSMM", "SMSM", "MSMS"]

solve2 :: [[Char]] -> Int
solve2 grid = length $ filter (xmasAtPos grid) $ findAs grid

main :: IO ()
main =
    do inLines <- lines <$> readFile "input"
       print $ solve1 inLines
       print $ solve2 inLines
