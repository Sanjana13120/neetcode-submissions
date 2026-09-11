class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total=0
        n=len(nums)

        for num in nums:
            total |= num

        return total<<(n-1)

'''

tc:O(n) 
sc:O(1)

5|1=5
5|6=7

7<<2==7*2^2=7*4=28

3,4,5,6,7,8
3|4=7
7|5=7
7|6=7
7|7=7
7|8=15

15<<5= 15*2^5=480
'''