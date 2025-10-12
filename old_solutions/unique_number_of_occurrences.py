from collections import Counter
from typing import List
# from itertools import pairwise

def uniqueOccurrences(arr: List[int]) -> bool:

    value_list = sorted([value for key, value in Counter(arr).items()])
    for a, b in pairwise(value_list):
        if a == b:
            return False
    return True



def test_uniqueOccurrences():
    arr = [1, 2, 2, 1, 1, 3]
    assert uniqueOccurrences(arr) == True
    arr = [1, 2]
    assert uniqueOccurrences(arr) == False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    assert uniqueOccurrences(arr) == True
