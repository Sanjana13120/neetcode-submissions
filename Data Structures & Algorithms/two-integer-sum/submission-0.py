class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]

            seen[num] = i


"""
tc: O(n)
sc: O(n)

nums = [3,4,5,6], target = 7

3 4 5 6
  i

seen = {}

i=0 target-num = 7-3=4 in seen?no

i=1 7-4=3 in num? yes 
return seen[target-num],i = 0,1

seen = {3:0}
---------------------------------------------------------
Input: nums = [4,5,6], target = 10

seen = {}

i=0 10-4 in seen? no seen={4:0}
i=1 10-5 in seen? no seen={4:0 5:1}
i=2 10-6 in seen? yes return seen[4],i = 0,2

"""
