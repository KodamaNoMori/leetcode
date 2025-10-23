from typing import List
import pytest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


def test_example_1():
    search_insert = Solution().searchInsert
    nums = [1, 3, 5, 6]
    target = 5
    expected_output = 2

    assert expected_output == search_insert(nums, target)

def test_example_2():
    search_insert = Solution().searchInsert
    nums = [1, 3, 5, 6]
    target = 2
    expected_output = 1

    assert expected_output == search_insert(nums, target)

def test_example_3():
    search_insert = Solution().searchInsert
    nums = [1, 3, 5, 6]
    target = 7
    expected_output = 4

    assert expected_output == search_insert(nums, target)

def test_negative_and_postive_in_list():
    search_insert = Solution().searchInsert
    nums = [-3, -2, -1, 0, 1, 3, 5, 6, 8, 12, 18]
    target = 7
    expected_output = 8

    assert expected_output == search_insert(nums, target)

def test_empty_list():
    search_insert = Solution().searchInsert
    nums = []
    target = 10
    expected_output = 0

    assert expected_output == search_insert(nums, target)

def test_negative_list():
    search_insert = Solution().searchInsert
    nums = [-8, -4, -2, -1]
    target = -3
    expected_output = 2

    assert expected_output == search_insert(nums, target)

def test_single_element_found():
    search_insert = Solution().searchInsert
    nums = [5]
    target = 5
    expected_output = 0

    assert expected_output == search_insert(nums, target)

def test_single_element_not_found():
    search_insert = Solution().searchInsert
    nums = [5]
    target = 3
    expected_output = 0

    assert expected_output == search_insert(nums, target)

def test_insert_at_beginning():
    search_insert = Solution().searchInsert
    nums = [1, 3, 5, 6]
    target = 0
    expected_output = 0

    assert expected_output == search_insert(nums, target)