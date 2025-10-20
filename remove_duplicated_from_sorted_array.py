import pytest
from typing import List
import pytest
from typing import List


class Solution:
    def __init__(self):
        pass

    def removeDuplicates(self, nums: List[int]) -> (int, List[int]):
        if not nums:
            return 0, nums

        write_index = 1

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        for i in range(write_index, len(nums)):
            nums[i] = None

        return write_index, nums


@pytest.fixture
def remove_dup_obj():
    return Solution().removeDuplicates

def test_input_list_len_eq_output_list_len_first(remove_dup_obj):
    input_list = None
    k = 20
    expected_output = None
    k_result, output_list = remove_dup_obj(nums=input_list)
    assert len(input_list) == expected_output
    assert k_result == k

def test_input_list_len_eq_output_list_len_first(remove_dup_obj):
    input_list = [1, 1, 2]
    k = 2
    expected_output = [1, 2, None]
    k_result, output_list = remove_dup_obj(nums=input_list)
    assert len(input_list) == len(output_list)
    assert k_result == 2
    assert output_list == expected_output

def test_input_list_len_eq_output_list_len_second(remove_dup_obj):
    input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = 5
    expected_output = [0, 1, 2, 3, 4, None, None, None, None, None]
    k_result, output_list = remove_dup_obj(nums=input_list)
    assert len(input_list) == len(output_list)
    assert k_result == k

def test_unique_elements_in_output_list(remove_dup_obj):
    pass

def test_element_between_min_and_max(remove_dup_obj):
    pass

def test_non_decreasing_order_in_output_list(remove_dup_obj):
    pass