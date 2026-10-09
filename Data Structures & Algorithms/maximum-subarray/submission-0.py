class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = maxsum = nums[0]

        for i in range(1, len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(maxsum, currsum)

        return maxsum


"""
tc: O(n)
sc: O(1)

goal - find the subarray with the largest sum and return the sum.

approach: kadane's algorithm 
since it has -ve and +ve nums

currsum = the largest sum of a subarray ending at the current index.
maxsum = the largest sum found anywhere so far.

currsum = max(currsum+nums[i], nums[i])
maxsum = max(maxsum, currsum)

Input: nums = [2,-3,4,-2,2,1,-1,4]

0  1 2  3 4 5  6 7
2 -3 4 -2 2 1 -1 4
                 i

currsum = 2
maxsum = 2

i=1 currsum = max(-3,-1)=-1
    maxsum = 2

i=2 currsum = max(4,3)=4
    maxsum=4

i=3 currsum = max(-2,2)=2
    maxsum=4

i=4 currsum = max(2,4)=4
    maxsum=4

i=5 currsum =max(1,5)=5
    maxsum=5

i=6 currsum = max(-1,4)=4
    maxum=5

i=7 currsum =max(4,8)=8
    maxsum = 8

"""
