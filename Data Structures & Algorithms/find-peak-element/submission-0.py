class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1

        while start<end:
            mid=start+(end-start)//2
            if nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid

        return start

'''
tc: O(logn)
sc: O(1)

goal - return the index to any of the peak 
peak ele means greater than its neighbors

Approach: binary search
Input: nums = [1,2,3,1]

0 1 2 3
1 2 3 1
    s e

start = 0
end = 3

mid=1 
nums[mid]< nums[mid+1] --> 2<3

start=2 end=3 mid =2
3>1 end=2

start=2 end=2

return start

-----------------------------------------------------------------

Input: nums = [1,2,1,3,4,5,0]

0 1 2 3 4 5 6
1 2 1 3 4 5 0
        s e

start=0 end=6 mid=3
3<4 yes start=4

start=4 end=6 mid=5
5>0 send=5

start=4 end=5 mid=4
4<5? start=5

start=5 end=5

return start=5




'''