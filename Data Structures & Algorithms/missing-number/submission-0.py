class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # optimal soln

        n = len(nums)
        # return (n*(n+1))//2 - sum(nums)
        xor = n

        for i in range(n):
            xor ^= i ^ nums[i]

        return xor


"""
otpimal soln
tc: O(n)
sc: O(1)

Approach 1: Mathematical Sum
Intuition: Calculate the expected sum of numbers from 0 to n, then subtract the actual array sum.

Expected sum = n * (n + 1) // 2
Missing number = expected sum - sum(nums)

Approach 2: XOR
Intuition: XOR all indices and array values, starting with xor = n. Matching numbers cancel out, leaving the missing number.

XOR properties
a ^ a = 0
a ^ 0 = a
XOR is associative and commutative.

Input: nums = [1,2,3]

xor=3

xor=3^0^1=2
xor=2^1^2=1
xor=1^2^3=0

----------------------------------------------------------------------------------------------------------------------------
"""

"""
----------------------------------------------------------------------------------------------------------------------------
Approach 3: Sorting
Intuition: Sort the array and compare each value with the expected number, starting from 0.

        nums.sort()

        miss = 0
        for i in range(len(nums)):
            if miss == nums[i]:
                miss += 1

        return miss

tc: O(nlogn)
sc: O(1)

Input: nums = [1,2,3]

missing = 0 
0==1? no 
0==2?no
0==3?no

return 0


--------------------------------------------
Input: nums = [0,2]
missing= 0

i=0 if 0==0 missing=1
i=1 2==1? no missing=1


"""
