class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res


"""
tc:  Sorting → O(n log n)
     Two-pointer search → O(n²)
     Overall → O(n^2)

Auxiliary Space:  O(1) -- Ignoring the output array `res`
                  O(n^2) - including output res

goal - return the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0 without any duplicates.

approach:

1. sort nums
2. Fix i and use two pointers
    i is the first number.
    left = i + 1
    right = len(nums) - 1
3. Check the sum
    total < 0 → left += 1
    total > 0 → right -= 1
    total == 0 → add the triplet and move both pointers.
4. Avoid duplicates
    i       → Have I already started a search with this value?
    left    → After finding a triplet, am I about to reuse the same left value?
    right   → After finding a triplet, am I about to reuse the same right value?


Input: nums = [-1,0,1,2,-1,-4]

res= []

  0 1  2 3 4 5
-4 -1 -1 0 1 2
    i    l  r

i=0
    left=1
    right=5

    -4-1+2= -3<0? left=2
    -4-1+2= -3<0 left=3
    -4+0+2= -2<0 left=4
    -4+1+2=-1<0 left=5

i=1
    left=2
    right=5

    -1-1+2==0 ?  res = [[-1,-1,2]]
    left=3 right=4
    -1+0+1==0? res = [[-1,-1,2], [-1,0,1]]
    left=4 right=3

i=2 i=3 and so on...

finally  res = [[-1,-1,2], [-1,0,1]]

--------------------------------------------------------------------






"""
