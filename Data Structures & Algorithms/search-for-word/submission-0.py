class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or c >= cols
                or r >= rows
                or board[r][c] == "#"
                or board[r][c] != word[i]
            ):
                return False

            board[r][c] = "#"

            res = (
                dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )

            board[r][c] = word[i]

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


"""
tc: O(m * 4^n)
sc: O(n)
m-  no of cells

given - board and word
goal - to check if word is present in the board by forming a path

approach: DFS + backtrack/recursion

   0 1 2 3
0  A B C D
1  S A A T
2  A C A E

1. Run the dfs for all cell
2. convert the word into list = [C,A,T]
3. if cell char is not equal to word char return false
4. mark the cell as visitedcheck for all directions= [(-1,0),(1,0),(0,-1),(0,1)]


dfs(0,0,0)
    A==C? no 
    return False

dfs(0,1,0)
    B==C? no False

dfs(0,2,0)    
    c==c?  mark it as #
    (-1,2,1) - X
    (1,2,1) - A==A? yes
        dfs(1,2,2)
            (0,2) - already #
            (2,2)  - A==T? no 
            (1,1) - A-==T no
            (1,3,2)  - T==T yes mark as #
                dfs(1,3,3)
                    3==len(word)? return true
       
    
   0 1 2 3
0  A B # D
1  S A # #
2  A C A E

------------------------------------------------------------------------
   0 1 2 3
0  A B C D
1  S A A T
2  A C A E


dfS(0,0,0)
    A==B? no
dfs(0,1,0)
    B==B yes amrk it as #
    up- X
    down - A==A? yes mark as #
    dfs(1,1,1)
        up-already marked
        down C==T?NO
        left= S==t?NO
        right= A==T?no
        remove # from 1,1
    right= C==A? no
    left= A==A? yes
    dfs(0,0,1)
        up- X
        left right down != T?
        remvoe # and make it A
remove # and make it B

return False


   0 1 2 3
0  A C C D
1  S A A T
2  A C A E

    



"""
