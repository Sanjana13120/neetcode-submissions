from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={0:1}

        for num in nums:
            new_dp=defaultdict(int)
            for total, count in dp.items():
                new_dp[total+num] +=count
                new_dp[total-num] +=count
            dp=new_dp

        return dp[target]

'''

tc: O(n*total)
sc: O(total)
 
goal - Return the number of different ways that you can build the expression such that the total sum equals target.


Input: nums = [2,2,2], target = 2

-2 +2 +2
+2 -2 +2
+2 +2 -2

approach: DP

{sum : ways}

base: {0:1}
choice: is either + or -
state: dp[sum] = no of ways to make the sum
transition: sum+num or sum-num
----------------------------------------------------------------------------------------------------------------
example
take first 2
+2 
-2

{2:1, -2:1}

take second 2
2+2=4
2-2=0
-2+2=0
-2-2=-4

{4:1, 0:2, -4:1}

take third 2
4+2=6
4-2=2

0+2=2
0-2=-2
0+2=2
0-2=-2

-4+2=-2
-4-2=-6

{6:1, 2:3, -2:3, -6:1}

target = 2
answer = 3

dp={0:1}

num=2
newdp={}
newdp={2:1, -2:1}
dp={2:1, -2:1}

num=2
newdp={}
newdp={4:1 0:2 -4:1}
dp={4:1 0:2 -4:1}

num=2
newdp={}
newdp={6:1 2:3 -2:3, -6:1}
----------------------------------------------------------------------------------------------------------------
'''


