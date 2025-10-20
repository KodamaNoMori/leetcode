from typing import List
import pytest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index and num_to_index[complement] != i:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        return []


@pytest.fixture(scope="function")
def solution_two_sum_object():
    solution = Solution()
    return solution.twoSum

def test_sum_1(solution_two_sum_object):
    nums = [2, 7, 11, 15]
    target = 9
    expected_output = [0,1]
    assert expected_output == solution_two_sum_object(nums, target)

def test_sum_2(solution_two_sum_object):
    nums = [3, 2, 4]
    target = 6
    expected_output = [1,2]
    assert expected_output == solution_two_sum_object(nums, target)


def test_sum_3(solution_two_sum_object):
    nums = [3, 3]
    target = 6
    expected_output = [0,1]
    assert expected_output == solution_two_sum_object(nums, target)

