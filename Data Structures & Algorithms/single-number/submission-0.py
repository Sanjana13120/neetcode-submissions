class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res


"""
tc: O(n)
sc: O(1)

Goal: Return the integer that appears only once.


Approach 1: Hash Set
- Track numbers to identify the unique element.
- Time: O(n)
- Space: O(n)

Approach 2: Bitwise XOR (Optimal)
- XOR all elements together.
- Duplicate numbers cancel out because a ^ a = 0.
- The unique number remains because a ^ 0 = a.
- XOR is commutative and associative, so order doesn't matter.

Input: nums = [3,2,3]

res=0

11
10
01
11
10

----------------------------------------------------------
Input: nums = [7,6,6,7,8]

7^6^6^7^8 = 8

111
110
001
110
111
111
0000
1000
1000




"""
