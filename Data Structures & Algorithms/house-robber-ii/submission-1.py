class Solution:
    def helper(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0],nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b)

        return b

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

'''
tc: O(n)
sc: O(1)

The circular-problem logic is exactly the same. The only optimization is inside helper().

Previously: dp[i] = max(dp[i-1], nums[i] + dp[i-2])

To calculate dp[i], we only need: dp[i-2] and dp[i-1]

We don't need the entire DP array.

a = dp[i-2]
b = dp[i-1]

After calculating the new value:

new_dp = max(a + nums[i], b)
'''