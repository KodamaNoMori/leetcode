# from typing import List
# # https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
# # TODO optimise
# def findMaxAverage(nums: List[int], k: int) -> float:
#     j = 0
#     max_avg = 0
#     relative_avg = 0
#
#     while j <= len(nums)-k:
#         for i in range(j, k + j):
#             relative_avg += nums[i] / k
#         [if (max_avg == 0) | (relative_avg > max_avg)]:
#             max_avg = relative_avg
#
#         j += 1
#         relative_avg = 0
#
#     return max_avg
#
# def test_maxAvgSubarray():
#     nums = [1, 12, -5, -6, 50, 3]
#     k = 4
#     assert findMaxAverage(nums, k) == 12.75
#     nums = [5]
#     k = 1
#     assert findMaxAverage(nums, k) == 5.00
#     nums = [-1]
#     k = 1
#     assert findMaxAverage(nums, k) == -1
#     nums = [0]
#     k = 1
#     assert findMaxAverage(nums, k) == 0
