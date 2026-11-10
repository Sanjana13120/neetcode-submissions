class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            count = count + 1 if num == 1 else 0
            res = max(count, res)

        return res


"""
tc: O(n)
sc: O(1)

goal - return the maximum number of consecutive 1's in the array.

Approach: Greedy / Single Pass

1. Initialize two variables:
   - count = 0: Tracks the current consecutive sequence of 1's.
   - res = 0: Stores the maximum consecutive 1's found so far.

2. Traverse the array:
   - If the current element is 1, increment count.
   - If the current element is 0, reset count to 0 because the consecutive sequence breaks.
   - Update res = max(res, count) at every iteration to keep track of the maximum sequence.

3. Return res.

--------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,1,0,1,1,1]

count = 0 
res = 0 

num=1 count=1 res=1
num=2 count=2 res=2
num=0 count=0 res=2
num=1 count=1 res=2
num=2 count=2 res=2
num=1 count=3 res=3

return res=3

--------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,0,1,1,0,1]

count=res=0

num=1 count=1 res=1
num=0 count=0 res=1
num=1 count=1 res=1
num=1 count=2 res=2
num=0 count=0 res=2
num=1 count=1 res=2

return res=2



"""
