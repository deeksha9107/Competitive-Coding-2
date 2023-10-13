# 1. Two Sum (https://leetcode.com/problems/two-sum/)
# // Time Complexity :O(n)
# // Space Complexity :O(n)
# // Did this code successfully run on Leetcode :Yes
# // Any problem you faced while coding this :No


# // Your code here along with comments explaining your approach
class Solution:
    def twoSum(self, nums, target):
        hmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hmap:
                return [i, hmap[difference]]
            hmap[nums[i]] = i
        return [-1, -1]


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))
