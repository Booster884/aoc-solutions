import Control.Applicative
import Text.ParserCombinators.ReadP
import Data.Bits
import Data.Char (isAlphaNum, isDigit)
import qualified Data.Map as M

data Gate = AndGate | OrGate | XorGate
    deriving (Show)
data Var = Value Int | Expr (Gate, String, String)
    deriving (Show)

nameP :: ReadP String
nameP = many1 $ satisfy isAlphaNum

valueP :: ReadP (String, Var)
valueP = do
    name <- nameP
    string ": "
    value <- Value . read <$> (string "0" <|> string "1")
    pure (name, value)

gateP :: ReadP Gate
gateP = (AndGate <$ string "AND")
        <|> (OrGate <$ string "OR")
        <|> (XorGate <$ string "XOR")

exprP :: ReadP (String, Var)
exprP = do
    a_name <- nameP
    skipSpaces
    gate <- gateP
    string " "
    b_name <- nameP
    string " -> "
    out_name <- nameP
    return (out_name, Expr (gate, a_name, b_name))

inputP :: ReadP (M.Map String Var)
inputP = do
    values <- sepBy valueP (char '\n')
    string "\n\n"
    exprs <- sepBy exprP (char '\n')
    return (M.fromList $ values ++ exprs)

evalGate :: Gate -> Int -> Int -> Int
evalGate AndGate a b = a .&. b
evalGate OrGate a b = a .|. b
evalGate XorGate a b = a `xor` b

eval :: M.Map String Var -> String -> Int
eval m k = case val of
    Value x -> x
    Expr (gate, a, b) -> evalGate gate (eval m a) (eval m b)
    where val = m M.! k

calculate :: M.Map String Var -> Int
calculate inp = sum $ zipWith shift bits [0..]
    where bits = map (eval inp) outputNames
          outputNames = map fst $ M.toList $ M.filterWithKey (\(k:_) _ -> k == 'z') inp

solve1 = calculate

solve2 = undefined

main :: IO ()
main =
    do inp <- fst . last . readP_to_S inputP <$> readFile "input"
       print $ solve1 inp
       -- print $ solve2 inLines
