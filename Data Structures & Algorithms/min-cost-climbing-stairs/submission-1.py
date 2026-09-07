class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #optimized space approach
        n=len(cost)

        prev1 = 0
        prev2 = 0
        

        for i in range(2,n+1):
            min_cost = min(prev1+cost[i-1], prev2+cost[i-2])
            prev2=prev1
            prev1= min_cost

        return prev1

'''
tc: O(n)
sc: O(1)

prev1 = 0
prev2 = 0

Input: cost = [1,2,3]

i=2, 3

i=2
min_cost = min(prev1+cost[i-1], prev2+cost[i-2])
         = min(2, 1)=1
prev2= prev1  = 0
prev1= min_cost = 1

i=3
min_cost = min(4, 2)=2

prev2=1
prev1=2
-----------------------------------------------------------------------
Input: cost = [1,2,1,2,1,1,1]

prev1=0 prev2=0
i=2,3...7

i=2
mincost= min(2,1)=1
prev2=0 prev=1

i=3
mincost= min(2,2)=2
prev2=1 prev1=2

i=4
min_cost = min(4,2)=2
prev2=2 prev1=2

i=5
min_cost =min(3, 4)=3
prev2=2 prev1=3

i=6
min_cdost = min(4, 3)=3
prev2=3 prev1=3

i=7
min_cost= min(4, 4)=4
prev2=3 prev1=4

return 4



'''