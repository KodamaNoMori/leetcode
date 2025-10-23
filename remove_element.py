from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pos = 0

        for read_pos in range(len(nums)):
            if nums[read_pos] != val:
                nums[write_pos] = nums[read_pos]
                write_pos += 1

        return write_pos


def test_example_0():
    remove_elements = Solution().removeElement

    nums = [3,1,3,3,2]
    val = 3
    expected_k = 2

    assert expected_k == remove_elements(nums, val)

def test_example_1():
    remove_elements = Solution().removeElement

    nums = [3,2,2,3]
    val = 3
    expected_k = 2

    assert expected_k == remove_elements(nums, val)


def test_example_2():
    remove_elements = Solution().removeElement

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expected_k = 5

    assert expected_k == remove_elements(nums, val)

def test_all_values_match():
    remove_elements = Solution().removeElement

    nums = [1, 1, 1]
    val = 1
    expected_k = 0

    assert expected_k == remove_elements(nums, val)


def test_all_values_no_match():
    remove_elements = Solution().removeElement

    nums = [1, 1, 1]
    val = 0
    expected_k = 3

    assert expected_k == remove_elements(nums, val)


def test_empty_array():
    remove_elements = Solution().removeElement
    nums = []
    val = 1
    expected_k = 0
    assert expected_k == remove_elements(nums, val)


def test_single_element_match():
    remove_elements = Solution().removeElement
    nums = [5]
    val = 5
    expected_k = 0
    assert expected_k == remove_elements(nums, val)


def test_single_element_no_match():
    remove_elements = Solution().removeElement
    nums = [5]
    val = 3
    expected_k = 1
    assert expected_k == remove_elements(nums, val)


def test_negative_values():
    remove_elements = Solution().removeElement
    nums = [-1, -2, -1, 3]
    val = -1
    expected_k = 2
    assert expected_k == remove_elements(nums, val)


def test_array_structure_verification():
    remove_elements = Solution().removeElement
    nums = [1, 2, 3, 2, 4]
    val = 2
    k = 3

    assert k == remove_elements(nums, val)
