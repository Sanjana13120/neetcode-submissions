class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1

        return count


'''
tc: O(1)
sc: O(1)

optimized soln
Approach: Brian Kernighan's Algorithm

Key idea:

n & (n - 1) removes the rightmost set bit (1).
Each iteration removes exactly one 1 bit.
Loop runs until n becomes 0.

Input: n = 23

Binary: 10111

Initial: count = 0

Iteration 1:
n = 10111 (23)
n - 1 = 10110 (22)
10111 & 10110 = 10110
n = 22, count = 1

Iteration 2:
n = 10110 (22)
n - 1 = 10101 (21)
10110 & 10101 = 10100
n = 20, count = 2

Iteration 3:
n = 10100 (20)
n - 1 = 10011 (19)
10100 & 10011 = 10000
n = 16, count = 3

Iteration 4:
n = 10000 (16)
n - 1 = 01111 (15)
10000 & 01111 = 00000
n = 0, count = 4

'''