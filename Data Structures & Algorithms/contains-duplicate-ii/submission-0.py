class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i

        return False


"""
tc: O(n)
sc: O(n)

goal - return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

Input: nums = [1,2,3,1], k = 3

seen = {}

num=1,i=0 in seen? no seen={1:0}
num=2,i=1 in seen? no seen={1:0,2:1}
num=3,i=2 in seen? no seen={1:0,2:1,3:2}
num=1,i=3 in seen? yes 
        3-seen[1]=3-0<=3? yes return true


-----------------------------------------------------------------------------------------------------------------
Input: nums = [2,1,2], k = 1
    
seen = {}

num=2,i=0 in seen? no seen={2:0}
num=1,i=1 in seen? no seen={2:0, 1:1}
num=2,i=2 in seen? yes 
        2-0=2<=1? no return false

"""
