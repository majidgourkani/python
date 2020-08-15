from pprint import pprint as PrettyPrinter
from copy import copy,deepcopy

array_2d = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18]]
PrettyPrinter(array_2d)

sample = ["a" , "b" , "c" , "d"]
array_2d1 = [sample , sample , sample]
PrettyPrinter(array_2d1)
array_2d1[0][0] = "A"
PrettyPrinter(array_2d1)

sample = ["a" , "b" , "c" , "d"]
array_2d2 = [copy(sample) , copy(sample) , copy(sample)]
PrettyPrinter(array_2d2)
array_2d2[0][0] = "A"
PrettyPrinter(array_2d2)
