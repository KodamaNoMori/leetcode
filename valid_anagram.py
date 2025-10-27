import pytest
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)  != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t

def test_example_1():
    is_anagram = Solution().isAnagram

    s = "anagram"
    t = "nagaram"
    expected_output = True

    assert expected_output == is_anagram(s,t)


def test_example_2():
    is_anagram = Solution().isAnagram

    s = "sdfljkasjdlf"
    t = "sdflj"
    expected_output = False

    assert expected_output == is_anagram(s,t)

def text_example_3():
    is_anagram = Solution().isAnagram

    s = "ttcvz"
    t = "aahlk"
    expected_output = False

    assert expected_output == is_anagram(s,t)

def text_example_4():

    is_anagram = Solution().isAnagram

    s = "hello"
    t = "hello"
    expected_output = True

    assert expected_output == is_anagram(s,t)

def text_example_5():

    is_anagram = Solution().isAnagram

    s = ""
    t = ""
    expected_output = True

    assert expected_output == is_anagram(s,t)
