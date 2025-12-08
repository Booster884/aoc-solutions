{-# LANGUAGE OverloadedStrings #-}

import Data.List (sort, sortBy)
import Data.Map.Strict qualified as M
import Data.Ord (Down (..), comparing)
import Data.Text qualified as T
import GHC.Float (int2Float)

-- Disjoint set functions
-- Inspired by Data.DisjointSet from disjoint-containers, but way less safe and efficient.

data DisjSet a = DisjSet
  !(M.Map a a) -- Parents
  !(M.Map a Int) -- Ranks; only roots have a rank.

empty :: DisjSet a
empty = DisjSet M.empty M.empty

insert :: (Ord a) => a -> DisjSet a -> DisjSet a
insert x ds@(DisjSet p r) =
  let p' = M.insert x x p
      r' = M.insert x 1 r
   in DisjSet p' r'

find :: (Ord a) => a -> DisjSet a -> a
find x ds@(DisjSet p _) =
  let x' = p M.! x
   in if x == x' then x else find x' ds

union :: (Ord a) => a -> a -> DisjSet a -> DisjSet a
union x y ds@(DisjSet p r) =
  let reprX = find x ds
      reprY = find y ds
   in if reprX == reprY
        then ds
        else
          let rankX = r M.! reprX
              rankY = r M.! reprY
           in case compare rankX rankY of
                LT ->
                  let p' = M.insert reprX reprY p
                      r' = M.delete reprX r
                   in DisjSet p' r'
                GT ->
                  let p' = M.insert reprY reprX p
                      r' = M.delete reprY r
                   in DisjSet p' r'
                EQ ->
                  let p' = M.insert reprX reprY p
                      r' = M.delete reprX $ M.insert reprY (rankY + 1) r
                   in DisjSet p' r'

flatten :: (Ord a) => DisjSet a -> M.Map a [a]
flatten ds@(DisjSet p x) =
  foldr
    (\x m -> M.insertWith (++) (find x ds) [x] m)
    M.empty
    $ M.keys p

sets :: DisjSet a -> Int
sets ds@(DisjSet _ r) = M.size r

-- Problem-related stuff

type Point = (Int, Int, Int)

parse :: T.Text -> [Point]
parse = map ((\[x, y, z] -> (x, y, z)) . (map (read . T.unpack) . T.splitOn ",")) . T.lines

distSquared :: Point -> Point -> Int
distSquared (x0, y0, z0) (x1, y1, z1) = (dx ^ 2 + dy ^ 2 + dz ^ 2)
  where
    dx = x0 - x1
    dy = y0 - y1
    dz = z0 - z1

closestConns points = sort [(distSquared a b, (a, b)) | a <- points, b <- points, a < b]

part1 points n =
  foldr1 (*) $
    take 3 $
      sortBy (comparing Down) $
        map length $
          M.elems $
            flatten $
              foldr (\(_, (a, b)) acc -> union a b acc) ds $
                take n $
                  closestConns points
  where
    ds = foldr (insert) empty points

part2 points = (\((a, _, _), (b, _, _)) -> a * b) $ f ds $ closestConns points
  where
    ds = foldr (insert) empty points
    f ds ((_, (a, b)) : xs) =
      let ds' = union a b ds
       in if sets ds' == 1 then (a, b) else f ds' xs

main = do
  testPoints <- parse . T.pack <$> readFile "test"
  points <- parse . T.pack <$> readFile "input"

  print $ part1 testPoints 10
  print $ part2 testPoints

  print $ part1 points 1000
  print $ part2 points
