from math import floor, ceil


def reverseVowels(s: str) -> str:
    vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
    str_len = len(s)
    left_pointer = 0
    right_pointer = str_len-1
    str_to_lst = list(s)

    while left_pointer < right_pointer:
        if s[left_pointer] not in vowels:
            left_pointer += 1
        elif s[right_pointer] not in vowels:
            right_pointer -= 1
        else:
            (str_to_lst[left_pointer]
             , str_to_lst[right_pointer]) = str_to_lst[right_pointer], str_to_lst[left_pointer]
            left_pointer += 1
            right_pointer -= 1
    return "".join(str_to_lst)


def test_reversed_vowels():
    s = "hello"
    assert reverseVowels(s) == "holle"
    s = "leetcode"
    assert reverseVowels(s) == "leotcede"