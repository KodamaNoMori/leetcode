from typing import List
import math
from collections import Counter

nums = [1,2,3,1,1,3]

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
#         # Solution 1
#         # Space complexity O(1)
#         # Time complexity O(n^2)
#         # total = 0
#         # for index, number in enumerate(nums):
#         #     for second_index in range(index+1, len(nums)):
#         #         if number == nums[second_index]:
#         #             total+=1
#
#         # Solution 2
#         # _dict = {}
#         # for num in nums:
#         #     if num in _dict:
#         #         _dict[num] += 1
#         #    else:
#         #        _dict[num] = 1
#         # print(sum(x for k, x in _dict.items() if x > 1))
#         # print(sum([math.comb(value, 2) for key, value in _dict.items()]))

        # Solution 3
        return sum([math.comb(value, 2) for key, value in Counter(nums).items()])
        # print(Counter(nums))
Solution().numIdenticalPairs(nums)