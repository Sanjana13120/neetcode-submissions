class Solution:
    def helper(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))


"""
tc: O(n)
sc: O(n)

goal - Return the maximum amount of money you can rob without alerting the police.

given houses are arranged in a circle, i.e. the first house and the last house are neighbors and you cannot rob two adjacent houses

Input: nums = [2,9,8,3,6]

Approach: DP

1. So split the circular problem into two linear House Robber problems:
2. Exclude the last house → nums[:-1]
   Exclude the first house → nums[1:]
3. Solve both and take the maximum.

base: dp[0]=nums[0]
      dp[1]=max(nums[0],nums[1])

choice: either rob - nums[i] + dp[i-2]
        or dont rob - dp[i-1]

states: dp[i] = maximum money we can rob from houses 0 to i.

transition: dp[i]=max(dp[i-1],nums[i]+dp[i-2])

[2,9,8,3] 
dp=[2 9 11 12]


[9,8,3,6]
dp=[9 9 12 15]

max of both dp = 15

"""
