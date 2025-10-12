# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    # word1_set = set(word1) # n
    # word2_set = set(word2) # n
    word1_dict = Counter(word1)
    word2_dict = Counter(word2)
    if word1_dict.keys() != word2_dict.keys():
        return False

    if Counter(word1_dict.values()) != Counter(word2_dict.values()):
        return False

    # word1_dict = [value for key, value in Counter(word1).items()] # 2n = n
    # word2_dict = [value for key, value in Counter(word2).items()] # 2n = n

    # for count in word1_dict: # n
    #     if count in word2_dict: # n
    #         index = word2_dict.index(count)
    #         del word2_dict[index]
    #     else:
    #         return False

    return True


def test_findIndex():
    word1 = "abc"
    word2 = "bca"
    assert closeStrings(word1, word2) == True
    word1 = "abcabc"
    word2 = "aacbcc"
    assert closeStrings(word1, word2) == False
    word1 = "abc"
    word2 = "abc"
    assert closeStrings(word1, word2) == True
    word1 = "abc"
    word2 = "bcc"
    assert closeStrings(word1, word2) == False
    word1 = "a"
    word2 = "aa"
    assert closeStrings(word1, word2) == False
    word1 = "cabbba"
    word2 = "abbccc"
    assert closeStrings(word1, word2) == True
