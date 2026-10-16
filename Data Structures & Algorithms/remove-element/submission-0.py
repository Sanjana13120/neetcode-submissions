class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0

        for num in nums:
            if num==val:
                continue
            
            nums[k]=num
            k+=1

        return k

'''
tc: O(n)
sc: O(1)

goal - remove ele and return k
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.





'''