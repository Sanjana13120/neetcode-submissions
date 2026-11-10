class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])  --> tc: O(n) sc: O(n)

        i = len(s) - 1
        count = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count


"""
tc: O(n)
sc: O(1)

Approach: Reverse Traversal (Single Pointer)

1. Start traversing the string from the last index using i = len(s) - 1.
2. Initialize count = 0 to track the length of the last word.
3. Skip all trailing spaces by moving i backwards until a non-space character is found.
4. Once a non-space character is found, start counting characters.
5. Continue moving backwards and increment count until:
   - A space is encountered, or
   - The beginning of the string is reached.
6. Return count.

----------------------------------------------------------------------------------------------------------------------------
Input: s = "Hello World"

0 1 2 3 4 5 6 7 8 9 10
H e l l o # W o r l d

i=10 d count=1
i=9  l count=2
i=8  r count=3
i=7  r count=4
i=6  W count=5
i=5 "" count=5 stop

return count=5
----------------------------------------------------------------------------------------------------------------------------

Input: s = "   fly me   to   the moon  "

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
# # # f l y # m e #  #  #  t  o  #  #  t  h  e  #  m  o  o  n  #  # 

i=25 # skip 
i=24 # skip
i=23 count=1
i=22 count=2
i=21 count=3
i=20 count=4
i=19 # stop

return count=4

"""
