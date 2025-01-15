# 3264. Final Array State After K Multiplication Operations I
# Easy

# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

 

# Example 1:

# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

# Output: [8,4,6,5,6]

# Explanation:

# Operation	Result
# After operation 1	[2, 2, 3, 5, 6]
# After operation 2	[4, 2, 3, 5, 6]
# After operation 3	[4, 4, 3, 5, 6]
# After operation 4	[4, 4, 6, 5, 6]
# After operation 5	[8, 4, 6, 5, 6]
# Example 2:

# Input: nums = [1,2], k = 3, multiplier = 4

# Output: [16,8]

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 10^5
# 1 <= multiplier <= 10^9   

# Follow up:

# Can you solve this problem in O(n) time complexity?   

# Solution:

# The problem is to find the minimum value x in nums and replace it with x * multiplier. We can use a min heap to find the minimum value and replace it with x * multiplier.

# Time complexity: O(n log n)
# Space complexity: O(n)        

# Code:

import heapq
from typing import List


class Solution:
    def finalArrayStateAfterKMultiplicationOperations(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heapq.heapify(nums)
        for _ in range(k):
            x = heapq.heappop(nums)
            heapq.heappush(nums, x * multiplier)
        return nums
