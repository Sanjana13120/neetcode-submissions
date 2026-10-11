class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


"""
tc: O(n)
sc: O(n) worst case; O(1) auxiliary space otherwise.

goal - Return the digits of the given integer after incrementing it by one.

Approach:

1. Start from the last digit and iterate from right to left.
2. If the current digit is less than 9, increment it by 1 and return the list immediately.
3. If the current digit is 9, change it to 0 and continue to the previous digit.
4. If the loop finishes, all digits were 9. Return [1] + digits to handle the extra digit.

Input: digits = [1,2,3,4]

i=3 4<9? yes 4+1=5 digits[3]=5
reutrn [1,2,3,5]

---------------------------------------------------------
Input: digits = [9,9,9]

i=2 9<9? no digits[2]=0 --> [9,9,0]
i=1 9<9? no digits[1]=0 --> [9,0,0]
i=0 9<9? no digits[0]=0 --> [0,0,0]

return [1]+digits = [1,0,0,0]



"""
