import pytest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_pos = 1

        for read_pos in range(1, len(nums)):
            if nums[read_pos] != nums[read_pos - 1]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1

        return write_pos


def test_input_list_len_eq_output_list_len_first():
    remove_dups = Solution().removeDuplicates

    input_list = [1, 1, 2]
    k = 2

    assert k == remove_dups(nums=input_list)

def test_input_list_len_eq_output_list_len_second():
    remove_dups = Solution().removeDuplicates

    input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = 5

    assert k == remove_dups(nums=input_list)

def test_all_duplicates():
    remove_dups = Solution().removeDuplicates

    input_list = [0, 0, 0, 0]
    k = 1

    assert k == remove_dups(nums=input_list)

def test_len_one_list():
    remove_dups = Solution().removeDuplicates

    input_list = [10]
    k = 1

    assert k == remove_dups(nums=input_list)

def test_no_duplicates():
    remove_dups = Solution().removeDuplicates

    input_list = [1,2,3,4]
    k = 4

    assert k == remove_dups(input_list)