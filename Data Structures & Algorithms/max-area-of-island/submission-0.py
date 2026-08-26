class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        maxcount=0

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 0

            grid[i][j]=0

            return 1 + dfs(i-1,j)+ dfs(i+1,j)+dfs(i,j-1)+ dfs( i,j+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    maxcount=max(maxcount,dfs(i,j))

        return maxcount
        
'''
tc: O(r*c)
sc: O(r*c)


   0 1 2 3 4 
0  0 1 1 0 1
1  1 0 1 0 1
2  0 1 1 0 1
3  0 1 0 0 1


dfs approach
rows=5 cols=4
maxcount=0

loop over rows and cols
    grid[i][j]==1: if yes
        count=dfs(i,j)
        maxcount=max(maxcount,count)

dfs(i,j)
    base cond - boundary check and grid[i][j]==0 return 0
    
    otherwise mark grid[i][j]=0 as visited

    check all 4 dir dfs(i-1,j),dfs(i+1,j),dfs(i,j-1),dfs(i,j+1)
    and add 


grid[0][1]==1
dfs(0,1)- 5+1=6
    grid[0][1]=0
    dfs(-1,1) X
    dfs(1,1) X 
    dfs(0,0) X
    dfs(0,2) == 1 4+1=5
        grid[0][2]=0
            dfs(1,2)==1 = 3+1=4
                grid[1][2]=0
                    dfs(2,2) =2+1=3
                        grid[2][2]=0
                            dfs(2,1) = 1+1=2
                                grid[2][1]=0
                                    dfs(3,1) = 1+0
                                        grid[3][1]=0 
                                        return 1
                                            

   0 1 2 3 4 
0  0 0 0 0 1
1  1 0 0 0 1
2  0 0 0 0 1
3  0 0 0 0 1


return 1+dfs(up)+dfs(down)+dfs(left)+dfs(right)





'''