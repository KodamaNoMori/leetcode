from typing import List

import pytest



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [0]

        last_index = len(digits) - 1

        def one_over_increment(index, count_nine = 0):
            if digits[index] == 9:
                digits[index] = 0
                count_nine += 1
                one_over_increment(index - 1, count_nine)
            else:
                if (index == -1) & (count_nine > 0):
                    digits = [0] + digits
                digits[index+1] = digits[index+1] + 1

        one_over_increment(last_index)

        return digits

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

    digits = None
    expected_output = [0]

    assert expected_output == plus_one(digits=digits)


def test_example_5():
    plus_one = Solution().plusOne

    digits = [0, 0, 0]
    expected_output = [0, 0, 1]

    assert expected_output == plus_one(digits=digits)


def test_example_5():
    plus_one = Solution().plusOne

    digits = [9, 9, 9, 9]
    expected_output = [1, 0, 0, 0]

    assert expected_output == plus_one(digits=digits)


def test_example_6():
    plus_one = Solution().plusOne

    digits = [1, 9]
    expected_output = [2, 0]

    assert expected_output == plus_one(digits=digits)


def test_example_7():
    plus_one = Solution().plusOne

    digits = [1, 9, 3]
    expected_output = [1, 9, 4]

    assert expected_output == plus_one(digits=digits)

def test_example_8():
    plus_one = Solution().plusOne

    digits = [0]
    expected_output = [1]

    assert expected_output == plus_one(digits=digits)