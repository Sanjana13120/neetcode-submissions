class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero = ones = twos = 0

        for num in nums:
            if num==0:
                zero+=1
            elif num==1:
                ones+=1
            else:
                twos+=1
        
        i=0

        for _ in range(zero):
            nums[i]=0
            i+=1

        for _ in range(ones):
            nums[i]=1
            i+=1

        for _ in range(twos):
            nums[i]=2
            i+=1

        
"""
tc: O(n)
sc: O(1)
goal - sort the array in-place such that elements of the same color are grouped together

Approach: Counting Sort

1. Initialize three counters: zero, ones, and twos.
2. Traverse the array and count occurrences of 0, 1, and 2.
3. Initialize index i = 0.
4. Fill the array with 0s based on the zero count.
5. Fill the array with 1s based on the ones count.
6. Fill the remaining positions with 2s based on the twos count.


Input: nums = [1,0,1,2]

0 1 2 3
1 0 1 2

zeros=1
ones=2
twos=1

i=0 nums[0]=0 
i=1 nums[1]=1
i=2 num[2]=1
i=3 nums[3]=2

nums = [0 1 1 2]



"""
