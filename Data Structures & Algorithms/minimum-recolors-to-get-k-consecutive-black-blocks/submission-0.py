class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        count = float("inf")
        left = 0

        for right in range(len(blocks)):
            if blocks[right] == "W":
                white += 1

            if right - left + 1 == k:
                count = min(count, white)

                if blocks[left] == "W":
                    white -= 1

                left += 1

        return count


"""
tc: O(n)
sc: O(1)

goal - Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks

recolor the white block to make it black 

Approach: Sliding Window

1. Maintain a window of size k using left and right pointers.
2. Maintain a variable `white` to count the number of white blocks ('W') in the current window.
3. Expand the window by moving the right pointer.
   - If blocks[right] == 'W', increment white.
4. Once the window size becomes k:
   - Update the minimum operations using min(ans, white).
   - Remove the leftmost element from the window.
   - If blocks[left] == 'W', decrement white.
   - Move left forward.
5. Continue until all possible windows are checked.
6. Return the minimum white count.


Input: blocks = "WBBWWBBWBW", k = 7

0 1 2 3 4 5 6 7 8 9
W B B W W B B W B W 
  l
                  r

right=9
left=1
white=4

7==7? yes
count=min(inf,3)=3

7==7? yes 
count=min(3,3)=3


Input: blocks = "BWWWBB", k = 6

0 1 2 3 4 5
B W W W B B
          r
l

right=5
left=0
white=3

5-0+1==k? yes
count=min(inf,3)=3
left=0







"""
