class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0

        for i in range(k):
            if blocks[i] == "W":
                white += 1

        ans = white

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                white -= 1

            if blocks[i] == "W":
                white += 1

            ans = min(ans, white)

        return ans

"""
tc: O(n)
sc: O(1)

goal - Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks

recolor the white block to make it black 

Approach: Fixed-Size Sliding Window

1. Calculate the number of white blocks (W) in the first window of size k.
2. Initialize ans with the white count of the first window.
3. Slide the window one position to the right:
    - Remove the outgoing element at index i - k.
    - If the outgoing element is W, decrement white.
    - Add the incoming element at index i.
    - If the incoming element is W, increment white.
4. Update the minimum number of white blocks using ans = min(ans, white).
5. Continue until all windows of size k are checked.
6. Return ans.


"""