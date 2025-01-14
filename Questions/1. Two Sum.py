# 1. Two Sum
# Visited on 2024-12-03
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i],nums[j]]
    return []



# Test cases for the two_sum function
print(two_sum([2, 7, 11, 15], 9))  # Expected output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Expected output: [1, 2]
print(two_sum([3, 3], 6))          # Expected output: [0, 1]
print(two_sum([1, 2, 3, 4, 5], 9)) # Expected output: [3, 4]
print(two_sum([0, -1, 2, -3, 1], -2)) # Expected output: [1, 3]











 

# # Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# nums = [2,1,7,11,15]
# target = 9

# # print(range(len(nums)))
# # for i in range(len(nums)):
# #     for j in range(i+1, len(nums)):
# #         print(i, j)
# print(Solution().twoSum(nums, target))

