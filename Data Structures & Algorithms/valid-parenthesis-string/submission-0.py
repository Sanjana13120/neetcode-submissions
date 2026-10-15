class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == "(":
                low += 1
                high += 1

            elif ch == ")":
                low -= 1
                high -= 1

            else:
                low -= 1
                high += 1

            if low < 0:
                low = 0

            if high < 0:
                return False

        return low == 0


"""
tc: O(n)
sc: O(1)

goal - Return true if s is valid, otherwise return false.

conditions:
    1. ( must have )
    2. ( should be before )
    3. * can be treated either as ),(  or ""


approach:

( - increases open count
) - decreases open count
* 
    1. either increase
    2. or decrease
    3. same

so we use low and high 
low - min possible number of unmatched (
high - max possible number of unmatched (


if low<0:
    low=0 because the minimum number of unmatched opening parentheses cannot be negative.

if high<0:
    return False because there are too many closing parentheses.

At the end, return whether min_open == 0.

low = the minimum possible number of unmatched opening parentheses after considering all possible interpretations of *.

A valid string must have zero unmatched opening parentheses at the end.


Input: s = "((**)"

0 1 2 3 4
( ( * * )

i=0 low=1 high=1
i=1 low=2 high=2
i=2 * if ( low=3 high=3
      if ) low=1 high=1
      if "" low=2 high=2

    so low=1 high=3

i=3 low=0 high=2
i=4 low=-1 high=1
    low<= so low=0

return low==0



"""
