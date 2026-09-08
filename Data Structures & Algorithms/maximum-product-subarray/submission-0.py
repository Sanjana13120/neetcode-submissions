class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod = nums[0]
        maxprod = nums[0]
        tempmaxprod = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            tempmaxprod = max(nums[i], minprod*nums[i], maxprod*nums[i])
            minprod = min(nums[i], minprod*nums[i], maxprod*nums[i])
            maxprod = tempmaxprod

            ans = max(ans, maxprod)

        return ans        

'''
Tc : O(n)
Sc : O(1)
Input: nums = [2,4,-3,5]

2 4 -3 5
       i 

minprod = 2 
maxprod = 2
ans=2

i=1
minprod = 2
maxprod = 8

ans=8

i=2
minprod = -24
maxprod = -3

ans=8

i=3
minprod = -120
maxprod = 5  

ans=8
--------------------------------------------------------------------------------

Input: nums = [-3,4,-2]
minprod = -3
maxprod = -3
ans=-3

i=1
minprod = -12
maxprod = 4
ans=4

i=2
minprod = -8
maxprod = 24
ans=24




'''