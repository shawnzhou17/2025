# 3152. Special Array II
# Medium
# Fixed size sliding window
# for i in range(len(arr) - k + 1):
#     window = arr[i: i + k]
#     print(window)

# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.

# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

# Example 1:

# Input: nums = [3,4,1,2,6], queries = [[0,4]]

# Output: [false]

# Explanation:

# The subarray is [3,4,1,2,6]. 2 and 6 are both even.

# Example 2:

# Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

# Output: [false,true]

# Explanation:

# The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
# The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], Q: List[List[int]]) -> List[bool]:
        arr = [0] * (len(nums)-1)
        print("arr",arr)
        for i in range(1,len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                arr[i-1] = 0
            else:
                arr[i-1] = 1
        print("arr",arr)
        preSum = [1]
        for v in arr:
            preSum.append(preSum[-1] + v)

        res = []
        for s,e in Q:
            if preSum[e] - preSum[s] == e-s:
                res.append(True)
            else:
                res.append(False)
        return res
    # def specialArray(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     subQuery = []
    #     currentQuery = 0
    #     answer = []
    #     k = 2 # 2 is the number of elements in a pair
    #     print(len(queries))
    #     for q in queries:
    #         subQuery.append(nums[q[0]:q[1]+1])
    #     print(subQuery)
        
    #     for sub in subQuery:
    #         if len(sub) == 1:
    #             answer.append(True)
    #             continue
    #         for i in range(len(sub) - k + 1):
    #             window = sub[i: i + k]
    #             print("window",window)
    #             print(window,len(window))
    #             if len(window) == 1:
    #                 answer.append(True)
    #                 break
    #             if window[0] % 2 == window[1] % 2:
    #                 print(window,window[0] % 2 == window[1] % 2)
    #                 answer.append(False)
    #                 break
    #             elif window[0] % 2 != window[1] % 2 and i == len(sub) - k:
    #                 answer.append(True)
    #                 currentQuery += 1
    #         print("sub", sub)
    #         if len(answer) == len(queries):
    #             break
    #     return answer


# nums = [3,4,1,2,6]
# queries = [[0,4],[0,2],[2,3]]
# print(Solution().specialArray(nums, queries))

nums = [1,5,7,9,2,6]
queries = [[0,0]]
print(Solution().isArraySpecial(nums, queries))

