class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n==1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]

        # optimal
        # a=nums[0]
        # b= max(nums[0],nums[1])

        # for i in range(2,n):
        #     a,b = b, max(nums[i] + a, b)
        # return b

        # tc : O(n)  sc: O(1)

        '''
        1 1 3 3
        a=1 b=1
        a=1 b=4
        a=4 b=4

        2 9 8 3 6
        a=2 b=9
        a=9 b=10 
        a=10 b=12
        a=12 b=16

        '''
        

'''
tc: O(n)
sc: O(n)


goal - Return the maximum amount of money 
Rule: Cannot rob two adjacent houses.

Input: nums = [1,1,3,3]
0 1 2 3
1 1 3 3

dp = [0 0 0 0]

base case: dp[0] = nums[0]
           dp[1] = max(nums[0],nums[1])

states:  dp[i] - maximum money we can rob from houses 0 to i

if we rob i: nums[i]+dp[i-2]  
if we dont rob i: dp[i-1]

transition: 
        dp[i]=max(nums[i]+dp[i-2], dp[i-1])

dp = [1 1 4 4]
dp[n]=4

-------------------------------------------------------------------

Input: nums = [2,9,8,3,6]

dp = [2 9 10 12 16]
dp[n]=16

--------------------------------------------------------------------

nums = [7, 3, 12, 5]

dp = [7 7 19 19]


'''