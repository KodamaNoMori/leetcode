def isSubsequence(s: str, t: str) -> bool:

    if len(s) > len(t):
        return False

    prev_match_index = -1
    s_index = 0

    while s_index < len(s):

        sliced_t = t[prev_match_index+1:]

        if s[s_index] in sliced_t:
            if (prev_match_index < 0) | (prev_match_index < t.index(s[s_index], prev_match_index+1)):
                prev_match_index = t.index(s[s_index], prev_match_index+1)
            else:
                return False
        else:
            return False
        s_index += 1
    return True




def test_reversed_vowels():
    s = "abc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == True
    s = "abcb"
    t = "ahbgdcb"
    assert isSubsequence(s, t) == True
    s = "axc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == False
    s = "acb"
    t = "ahbgdc"
    assert isSubsequence(s, t) == False
    s = "acb"
    t = "ahcbgd"
    assert isSubsequence(s, t) == False