from typing import List

# class Solution:
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for index in reversed(range(len(nums))):
        if nums[index] == 0:
            nums.append(nums.pop(index))
    return nums


def test_zeroes_moved():
    nums = [0, 1, 0, 3, 12]
    assert moveZeroes(nums) == [1,3,12,0,0]
    nums = [0]
    assert moveZeroes(nums) == [0]