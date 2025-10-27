class Solution:
    @staticmethod
    def is_alphanumeric(char: str) -> bool:
        return 'a' <= char <= 'z' or '0' <= char <= '9'

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            if not self.is_alphanumeric(s[left]):
                left += 1
                continue

            if not self.is_alphanumeric(s[right]):
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    # def isPalindrome(self, s: str) -> bool:
    #     cleaned = ''.join(filter(str.isalnum, s.lower()))
    #
    #     return cleaned[::-1] == cleaned


def test_example_1():
    is_palindrome = Solution().isPalindrome
    s = "A man, a plan, a canal: Panama"
    expected_output = True
    assert expected_output == is_palindrome(s)

def test_example_2():
    is_palindrome = Solution().isPalindrome
    s = "race a car"
    expected_output = False
    assert expected_output == is_palindrome(s)

def test_example_3():
    is_palindrome = Solution().isPalindrome
    s = "  "
    expected_output = True
    assert expected_output == is_palindrome(s)

def test_example_4():
    is_palindrome = Solution().isPalindrome
    s = "a1b23ccab123 "
    expected_output = False
    assert expected_output == is_palindrome(s)

def test_example_5_empty():
    is_palindrome = Solution().isPalindrome
    s = ""
    expected_output = True
    assert expected_output == is_palindrome(s)
