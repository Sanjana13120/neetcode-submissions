class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r=len(board)
        c=len(board[0])

        def  dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or board[i][j]=="X" or board[i][j]=="#":
                return

            board[i][j]="#"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        for i in range(r):
            for j in range(c):
                if board[i][j]=="O" and (i==0 or j==0 or i==r-1 or j==c-1):
                    dfs(i,j)


        for i in range(r):
            for j in range(c):
                if board[i][j]=="#":
                    board[i][j]="O"

                elif board[i][j]=="O":
                    board[i][j]="X"        

'''
Time:  O(r*c)
Space: O(r*c)
   0 1 2 3 
0  x x x x
1  x o o x
2  x x o x
3  x o x x

dfs approach
r=4 c=4

traverse over rows and cols
    board[i][i]==0 and if its boundary- i==0 or j==0 or i==r-1 or j==c-1?
        dfs(i,j)

dfs(i,j)
    base condition is board[i][j]==x ? return

    and mark board[i][j]='#'
    basically keep checking if top left right botton has o? 

   0 1 2 3 
0  x x x x
1  x o o x
2  x x o x
3  x o x x

grid[1][1]==O but not boundary

grid[1][2]==O but not boundary

grid[2][2]==O but not boundary

grid[3][1]==O and boundary

    dfs(3,1)
        mark board[3][1]=#
        dfs(i-1,j), dfs(i+1,j), dfs(i,j-1) and dfs(i,j+1)


now this our final output

   0 1 2 3 
0  x x x x
1  x o o x
2  x x o x
3  x # x x

so loop over board[r][c] if # mark it O if O mark it X


    



'''