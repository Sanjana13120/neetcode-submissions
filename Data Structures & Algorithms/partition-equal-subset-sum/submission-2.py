class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:
            for curr in range(target, num - 1, -1):
                if dp[curr - num]:
                    dp[curr] = True

        return dp[target]


"""
TC: O(n * target)
SC: O(target)

goal - Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

approach: DP

Input: nums = [1,2,3,4]

1 2 | 3 4 == 3 | 7
1 3 | 2 4 == 4 | 6
1 4 | 2 3 == 5 | 5


find total 
if total is even we can partition 
if total is odd - false

total = 10
target= 10/2 =5

base: dp[0] = True → we can make sum 0 using no number

state: dp[i] = True means we can make a sum equal to i using the numbers processed so far.

transition:If dp[curr - num] is True, then we can make sum curr by adding num.

dp=[T 0 0 0 0 0]

num=1
    curr= 5,4,3,2,1
    dp[5-1]=F
    dp[4-1]=F
    dp[3-1]=F
    dp[2-1]=F
    dp[1-1]=T
        so dp=[T T 0 0 0 0]

num=2
    curr= 5,4,3,2
    dp[5-2]=F
    dp[4-2]=F
    dp[3-2]=T
    dp[2-2]=T
        so  dp=[T T T T 0 0]

num=3
    curr= 5,4,3
    dp[5-3]=T
    dp[4-3]=T
    dp[3-3]=T
        so   dp=[T T T T T T]

retrun dp[5]=T

------------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,5,11,5]

total=22
target=11

dp = [T, F, F, F, F, F, F, F, F, F, F, F]

num=1
    dp[0] is T
    dp[1-1]=T

    so dp = [T, T, F, F, F, F, F, F, F, F, F, F]

num=5
    curr=11,10,9,8,7,6,5
    dp[5-5]=T
    dp[6-5]=T

    so dp = [T, T, F, F, F, T, T, F, F, F, F, F]

num=11
    curr=11
    dp[11-11]=T
    so dp = [T, T, F, F, F, T, T, F, F, F, F, T]

num=5
    curr=11,10,9,8,7,6,5
    dp[11-6]=T
    dp[10-5]=T
    dp[6-5]=T
    dp[5-5]=T
    so dp = [T, T, F, F, F, T, T, F, F, F, T, T]


return dp[11]


"""
