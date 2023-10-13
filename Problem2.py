# 494. Target Sum (https://leetcode.com/problems/target-sum/)
# // Time Complexity : O(t.n)
# // Space Complexity : O(t.n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
class Solution:
    def findTargetSumWays(self, nums, target):
        self.target = target
        self.cache = {}
        self.length = len(nums)
        return self.helper(nums, 0, 0)

    def helper(self, nums, index, total):
        if (index, total) in self.cache:
            return self.cache[(index, total)]
        if index == self.length:
            if total == self.target:
                return 1
            else:
                return 0
        count = 0
        # logic
        count += self.helper(nums, index + 1, total + nums[index])
        count += self.helper(nums, index + 1, total - nums[index])
        self.cache[(index, total)] = count
        return count


nums = [1, 1, 1, 1, 1]
target = 3
sol = Solution()
print(sol.findTargetSumWays(nums, target))
