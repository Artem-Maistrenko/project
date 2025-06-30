# В последовательности на n целых элементов найти произведение элементов 
# средней трети. 
middleThirdProduct :: [Int] -> Int
middleThirdProduct xs = product $ take middleLength $ drop start xs
  where
    len = length xs
    start = (len - len `div` 3) `div` 2
    middleLength = len `div` 3

