class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxReach = 0
        jump = 0

        for i in range(len(nums) - 1):
            maxReach = max(maxReach, nums[i] + i)

            if i == end:
                jump += 1
                end = maxReach

        return jump

"""
tc: O(n)
sc: O(1)
goal - return the minimum number of jumps to reach the last position in the array

starting at nums[0] -- reach last index in min jump

conditions:
    j <= nums[i]
    i + j < nums.length

approach: Greedy

jump — number of jumps taken.
maxReach — farthest index reachable from the indices explored so far.
end — boundary of the current range.

1. Update maxReach using the current index and its jump length.
2. When i == end:
        Increment jump.
        Update end = maxReach.


----------------------------------------------------------------------------------------------------------
Input: nums = [2,4,1,1,1,1]

jump=0 maxReach=0 end=0

i=0  num=2  maxReach=2 0==0? jump=1 end=2
i=1  num=4  maxReach=5 1==2? no
i=2  num=1  maxReach=5 2==2? yes jump=2 end=5
i=3  num=1  maxReach=5 3==5? no 
i=4  num=1  maxReach=5 4==5? no

return jump=2



"""
