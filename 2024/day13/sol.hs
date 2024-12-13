import Text.ParserCombinators.ReadP
import Control.Applicative
import Data.Char (isDigit)

data ClawMachine = ClawMachine
    { moveA :: (Int, Int)
    , moveB :: (Int, Int)
    , prizePos :: (Int, Int)
    }
    deriving Show

offset :: Int -> ClawMachine -> ClawMachine
offset off ClawMachine {moveA, moveB, prizePos=(p0, p1)} =
    ClawMachine {moveA, moveB, prizePos=(p0 + off, p1 + off)}

digit :: ReadP Char
digit = satisfy isDigit

diff :: ReadP Int
diff = do
    -- Bit of a hack, but the input doesn't contain negative moves.
    char '+'
    read <$> count 2 digit

move :: ReadP (Int, Int)
move = do
    string "Button "
    button <- char 'A' <|> char 'B'
    string ": X"
    dx <- diff
    string ", Y"
    dy <- diff
    return (dx, dy)

prize :: ReadP (Int, Int)
prize = do
    string "Prize: X="
    x <- read <$> many1 digit
    string ", Y="
    y <- read <$> many1 digit
    return (x, y)

claw :: ReadP ClawMachine
claw = do
    moveA <- move
    char '\n'
    moveB <- move
    char '\n'
    prizePos <- prize
    return ClawMachine {moveA, moveB, prizePos}

claws :: ReadP [ClawMachine]
claws = sepBy claw (string "\n\n")

cost :: ClawMachine -> Int
cost ClawMachine {moveA=(a0, a1), moveB=(b0, b1), prizePos=(p0, p1)} =
    if possible then 3 * (n `div` det) + (m `div` det) else 0
    where det = a0 * b1 - b0 * a1
          n = p0 * b1 - p1 * b0
          m = a0 * p1 - a1 * p0
          possible = n `mod` det == 0 && m `mod` det == 0

solve :: Int -> [ClawMachine] -> Int
solve off = sum . map (cost . offset off)

main :: IO ()
main =
    do clawMachines <- fst . last . readP_to_S claws <$> readFile "input"
       print $ solve 0 clawMachines
       print $ solve 10000000000000 clawMachines
