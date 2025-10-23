from typing import List

import pytest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [0]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

def test_example_1():
    plus_one = Solution().plusOne

    digits = [1, 2, 3]
    expected_output = [1,2,4]

    assert expected_output == plus_one(digits = digits)


def test_example_2():
    plus_one = Solution().plusOne

    digits = [4,3,2,1]
    expected_output = [4,3,2,2]

    assert expected_output == plus_one(digits=digits)


def test_example_3():
    plus_one = Solution().plusOne

    digits = [9]
    expected_output = [1,0]

    assert expected_output == plus_one(digits=digits)


def test_example_4():
    plus_one = Solution().plusOne

    digits = [9, 9, 9, 9]
    expected_output = [1, 0, 0, 0, 0]

    assert expected_output == plus_one(digits=digits)


def test_example_5():
    plus_one = Solution().plusOne

    digits = [1, 9]
    expected_output = [2, 0]

    assert expected_output == plus_one(digits=digits)


def test_example_6():
    plus_one = Solution().plusOne

    digits = [1, 9, 3]
    expected_output = [1, 9, 4]

    assert expected_output == plus_one(digits=digits)

def test_example_7():
    plus_one = Solution().plusOne

    digits = [0]
    expected_output = [1]

    assert expected_output == plus_one(digits=digits)