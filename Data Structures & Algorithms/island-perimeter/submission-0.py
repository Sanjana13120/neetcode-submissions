class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1

            if grid[i][j] == "#":
                return 0

            grid[i][j] = "#"

            res = dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

            return res

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return dfs(i,j)

        return 0


"""
tc: O(r*c)
sc: O(r*c)

   0 1 2 3
0  1 1 0 0
1  1 0 0 0 
2  1 1 1 0
3  0 0 1 1


Approach: dfs

1. loop over rows and cols and run DFS for each cell grid[i][j]==1 
2. mark it as visited mayb grid[i][j]=#
3. check for up,down,left and right if grid[i][j]=0 then return 1 or out of boundary also return 1
else keep exploring

dfs(0,0)
    mark it as #
    up- x = 1
    left x = 2
    right is 1 
        dfs(0,1)
            mark as #
            up- 3
            left - x
            right- 0 4
            down- 0 5
    down is 1
        dfs(1,0)
            mark it as #
            up- x 
            left- 6
            right- 7
            down is 1
            dfs(2,0)
                mark it as #
                up- x
                left- 8
                down- 9
                right is 1
                dfs(2,1)
                    mark as #
                    up- 10
                    left- x
                    down - 11
                    right is 1
                    dfs(2,2)
                        mark as #
                        up - 12
                        left - x
                        right- 13
                        down is 1
                        dfs(3,2)
                            mark as viisted
                            up- x
                            left- 14
                            down- 15
                            right is 1
                            dfs(3,3)
                                mark as visited
                                up- 16
                                left- x
                                right - 17
                                down-18


   0 1 2 3
0  # # 0 0
1  # 0 0 0 
2  # # # 0
3  0 0 # #


final perimeter is 18

"""
