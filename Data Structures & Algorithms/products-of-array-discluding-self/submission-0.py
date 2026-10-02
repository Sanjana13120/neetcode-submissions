class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        left = 1
        right = 1

        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


"""
tc: O(n)
sc: O(n)

goal - return an array output where output[i] is the product of all the elements of nums except nums[i]. 

Input: nums = [1,2,4,6]

initialize res=[1]*len(nums)
1. scan left to right and find the left product
2. scan right to left and find the right product
3. multiply left and right product

left=[1 1 2 8]
right=[48 24 6 1]
res=[48 24 12 8]

res = [1 1 1 1]
left=1

i=0 res[0]=1 left=1
i=1 res[1]=1 left=2
i=2 res[2]=2 left=8
i=3 res[3]=8 left=48

res=[1 1 2 8]

right=1

i=3 res[3]=1*1=1 right=6
i=2 res[2]=2*6=12  right=24
i=1 res[1]=1*24=24 right=48
i=0 res[0]=1*48=48 right=48


res=[48 24 12 8]

-----------------------------------------------------------------------------

Input: nums = [-1,0,1,2,3]

left=[1 -1 0 0 0]
right=[0 6 6 3 1]
res= [0 -6 0 0 0]


"""
