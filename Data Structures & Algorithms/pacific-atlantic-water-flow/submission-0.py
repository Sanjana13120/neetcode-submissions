class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c)) in visit or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]< prevHeight:
                return

            visit.add((r,c))

            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])


        # top and bottom edge
        for c in range(cols):
            dfs(0,c,pacific_visited,heights[0][c])
            dfs(rows-1,c,atlantic_visited,heights[rows-1][c])

        # left and right edge
        for r in range(rows):
            dfs(r,0,pacific_visited,heights[r][0])
            dfs(r,cols-1,atlantic_visited,heights[r][cols-1])

        # Cells reachable from both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_visited and (r,c) in atlantic_visited:
                    res.append([r,c])

        return res
        
"""

tc: O(rows * cols)
sc: O(rows * cols)

two oceans-
pacific - top and left side
atlantic - bottom and right

directions = up,down,left,right

we hve to find cells whr water can flow to both pacific and atlantic ocean


top    = [0][c]
left   = [r][0]
bottom = [rows-1][c]
right  = [r][cols-1]

pacific_visited = set()
atlantic_visited = set()

1. Identify Pacific boundaries.
2. DFS inward and store reachable cells in pacific_visited.
3. Identify Atlantic boundaries.
4. DFS inward and store reachable cells in atlantic_visited.
5. Find the intersection of the two sets.
6. Return those coordinates.


height:   [4,2,7,3,4]
          [7,4,6,4,7]
          [6,3,5,3,6]

rows=3 cols=5

c -- 0,1,2,3,4

c=0
dfs(0,0,{},4)
    pacific_visited={(0,0)}
    top- X
    left- X
    right= dfs(0,1,{(0,0)},4)
            2<4 yes return
    bottom = dfs(1,0,{(0,0)},4)
            7<4? no
            pacific={(0,0),(1,0)}
c=1
dfs(0,1,{(0,0),(1,0)},2)
    pacific={(0,0),(1,0),(0,1)}
    top- x
    left - visited
    right- dfs(0,2,{(0,0),(1,0),(0,1)},2)
            7<2? no
            pacific={(0,0),(1,0),(0,1),(0,2)}
    bottom= dfs(1,1,{(0,0),(1,0),(0,1)},2)
            6<2? no
            pacific={(0,0),(1,0),(0,1),(0,2),(1,1)}


        





"""