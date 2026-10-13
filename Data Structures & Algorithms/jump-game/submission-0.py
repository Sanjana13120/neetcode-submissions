class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, nums[i] + i)

        return True


"""
tc: O(n)
sc: O(1)


goal - Return true if you can reach the last index starting from index 0, or false otherwise.

approach: Greedy

Key idea:
- nums[i] tells us the maximum jump length from index i.
- maxReach stores the farthest index we can reach so far.
- We should only process an index if we can actually reach it.

Reachability check:
If i > maxReach, the current index is unreachable, so return False.

Update maxReach:
maxReach = max(maxReach, i + nums[i])

This keeps the farthest reachable index instead of allowing it to move backward.


Input: nums = [1,2,0,1,0]

0 1 2 3 4
1 2 0 1 0

i=0 num=1 i can jump 1 step to idx 1
i=1 num=2 i can jump 2 step to idx 2,3
i=2 num=0 cannot jump
i=3 num=1 i can jump 1 step to idx 4 which is my last idx 

hence return true

soo keep tracking the maxRecach
maxReach = max(maxReach, nums[i]+i)

maxReach = 0
i=0 num=1 0>0? no maxReach=max(0,1+0)=1
i=1 num=2 1>1? no maxReach=max(1,3)=3
i=2 num=0 2>3? no maxReach=max(3,2)=3
i=3 num=1 3>3? no maxReach=max(3,4)=4
i=4 num=4 4>4? no maxReach=max(4,8)=8

hence we can reach idx 4-- return True

-----------------------------------------------------------------------------------------------------------
Input: nums = [1,2,1,0,1]

maxReach = 0
i=0 num=1 0>0?no maxReach=max(0,1)=1
i=1 num=2 1>1? no maxReach=max(1,3)=3
i=2 num=1 2>3? no maxReach=max(3,3)=3
i=3 num=0 3>3? no maxReach=max(3,3)=3
i=4 num=1 4>3? yes return False





"""
