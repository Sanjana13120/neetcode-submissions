from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


"""
tc: O(81) = O(1)
sc: O(81) = O(1)

We visit each cell once and perform O(1) hash set operations.
At most 81 values are stored across rows, columns, and squares.

goal - Return true if the Sudoku board is valid, otherwise return false

conditions:
1. each row must contain 1-9 without duplicates.
2. each column must contain 1-9 without duplicates.
3. this 9x9 board so each 3x3 sub box must contain 1-9 without duplicates.


approach: Hashset

1. for checking duplicates-- we can use set to track the seen
    rows={}
    cols={}
    squares={}
2. loop thorugh each r and c.
    if its '.' -- skip 
    if val is present in rows or cols or squares: 
        return false

    Identify the 3x3 square using: (r // 3, c // 3)

   Rows:
       0,1,2 -> 0
       3,4,5 -> 1
       6,7,8 -> 2

   Cols:
       0,1,2 -> 0
       3,4,5 -> 1
       6,7,8 -> 2

   Therefore all cells belonging to the same 3x3 box generate the same key.

   Example:
       (0,0) -> (0,0)
       (1,2) -> (0,0)
       (2,1) -> (0,0)

3. otherwise add to row[r],cols[c],squares[(r//3,c//3)]
4. finally return true 


Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

rows={} cols = {} sqaures = {}

board[0][0]=1 not in row not in cols and squares
rows={0:{1}} cols = {0:{1}} sqaures = {(0,0):{1}}

board[0][1]=2 not in any seen
rows={0:{1,2}} cols = {0:{1}, 1:{2}} sqaures = {(0,0):{1,2}}

board[0][2] and board[0][3] skip

board[0][4]=3 not in seen
rows={0:{1,2,3}} cols = {0:{1},4:{3}} sqaures = {(0,0):{1,2}, (0,1):{3}}

and so on...

so this is valid sudoku





"""
