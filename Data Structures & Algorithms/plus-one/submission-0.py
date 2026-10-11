class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""

        for i in range(len(digits)):
            str_num += str(digits[i])

        total = int(str_num) + 1

        
        
        return [int(digit) for digit in str(total)]


"""
tc: O(n)
sc: O(n)

goal - Return the digits of the given integer after incrementing it by one.

approach

1. Combine all digits into a string.
2. Convert the string into an integer and add 1.
3. Convert the result back into a string.
4. Convert each character into an integer and return the list.

"""
