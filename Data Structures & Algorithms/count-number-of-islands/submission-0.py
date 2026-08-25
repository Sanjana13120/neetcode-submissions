class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]=="0":
                return

            grid[i][j]="0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)

        return count
        

'''
tc: O(r*c)
sc: O(r*c)

   0 1 2 3 4
0  0 1 1 1 0
1  1 1 0 1 0
2  1 1 0 0 0
3  0 0 0 0 0

r=5  c=4
directions = [(-1,0),(1,0),(0,-1),(0,1)]

traverse over the grid[r][c]
dfs approach

grid[i][j]==1count=1
dfs(i,j)

dfs(i,j)-- here we will be checking all 4 directions and mark grid[i][j]=0
base condition- grid[i][j]==0: return

grid[0][1]==1

   0 1 2 3 4
0  0 0 0 0 0
1  0 0 0 0 0
2  0 0 0 0 0
3  0 0 0 0 0

count=1

--------------------------------------------------------------------------------------

   0 1 2 3 4 
0  1 1 0 0 1
1  1 1 0 0 1
2  0 0 1 0 0
3  0 0 0 1 1

grid[0][0]==1:
    count=1

dfs(0,0)

   0 1 2 3 4 
0  0 0 0 0 1
1  0 0 0 0 1
2  0 0 1 0 0
3  0 0 0 1 1

mark grid[0][0]=0 and check  all 4 direcitons using dfs(i-1,j), df(i+1,j),dfs(i,j-1),dfs(i,j+1)

grid[0][4]==1:
    count=2

   0 1 2 3 4 
0  0 0 0 0 0
1  0 0 0 0 0
2  0 0 1 0 0
3  0 0 0 1 1

mark grid[0][4]=0 and check  all 4 direcitons using dfs(i-1,j), df(i+1,j),dfs(i,j-1),dfs(i,j+1)

grid[2][2]==1
    count=3

   0 1 2 3 4 
0  0 0 0 0 0
1  0 0 0 0 0
2  0 0 0 0 0
3  0 0 0 0 0

mark grid[2][2]=0 and check  all 4 direcitons using dfs(i-1,j), df(i+1,j),dfs(i,j-1),dfs(i,j+1)

grid[3][3]==1:
    count=4

mark grid[3][3]=0 and check  all 4 direcitons using dfs(i-1,j), df(i+1,j),dfs(i,j-1),dfs(i,j+1)


return count=4




'''