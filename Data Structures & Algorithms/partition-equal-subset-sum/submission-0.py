class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        res = {0}

        for num in nums:
            for curr in list(res):
                new_sum = num + curr
                if new_sum == target:
                    return True
                res.add(new_sum)

        return False


"""
tc: O(n*sum(nums))
sc: O(sum(nums))

goal - Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

approach:

Input: nums = [1,2,3,4]

1 2 | 3 4 == 3 | 7
1 3 | 2 4 == 4 | 6
1 4 | 2 3 == 5 | 5


find total 
if total is even we can partition 
if total is odd - false

total = 10
target= 10/2 =5

res= {0}

loop over nums
    loop over res
        find new sum
            if newsum==target:
                return True
            add newsum to res

num=1
    res=0 0+1=1 res={0,1}
num=2
    res=0+2=2 res={0,1,2}
    res=1+2=3 res={0,1,2,3}
num=3
    res=0+3=3 res={0,1,2,3}
    res=1+3=4 res={0,1,2,3,4}
    res=2+3=5 5==target return True

----------------------------------------------------------------------------------------
Input: nums = [1,2,3,4,5]

total = 15%2 !=0 so false

"""
