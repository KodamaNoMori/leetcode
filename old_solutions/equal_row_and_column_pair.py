# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    return


def test_equalPairs():
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    assert equalPairs(grid) == 1
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    assert equalPairs(grid) == 3