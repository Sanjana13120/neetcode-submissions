from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        rows=len(grid)
        cols=len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
        
        while q:
            r,c=q.popleft()
                
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]== 2147483647:
                    grid[nr][nc]= grid[r][c]+1
                    q.append((nr,nc))

'''
tc: O(r*c)
sc: O(r*c)

Approach: Multi source BFS

since we have to travel level be level

we have to find the dist to nearest treasure (0)
-1 --> blocked 
from inf we have to find the nearest 0 else leave as inf

check all 4 directions = [(-1,0),(1,0),(0,-1),(0,1)]

append r,c in q for grid[i][j]==0
q=[(0,2),(3,0)]

until q is empty
    take one cell
    look at 4 neigbours
    if negihbour is inf
        dist=current_distance +1
        mark neighbor with dist 
        add neighbor to q

    0    1   2    3
0  inf  -1   0    inf
1  inf  inf  inf  -1 
2  inf  -1   inf  -1
3  0    -1   inf  inf

q=[(0,2),(3,0)]

dit=0

r=0 c=2 --- q=[(3,0)]
(-1,0) - nr=-1 nc=2 X
(1,0)  - nr=1 nc=2 its is inf append to q dist=1
(0,-1) - nr=0 nc=1 blocked
(0,1)  - nr=0 nc=3 its is inf append to q dist=1

    0    1   2    3
0  inf  -1   0    1
1  inf  inf  1   -1 
2  inf  -1   inf  -1
3  0    -1   inf  inf

q=[(3,0),  (1,2), (0,3)]

r=3 c=0  -- q=[(1,2), (0,1)]
(-1,0) - nr=2 nc=0  its is inf append to q dist=0+1=1
(1,0)  - nr=4 nc=0 X
(0,-1) - nr=3 nc=-1 x
(0,1)  - nr=3 nc=1 blocked

    0    1   2    3
0  inf  -1   0    1
1  inf  inf  1   -1 
2  1    -1   inf  -1
3  0    -1   inf  inf

dist=1
q=[(1,2), (0,3),  (2,0)]

r=1 c=2 - q=[(0,3),  (2,0)]
(-1,0) = nr=0 nc=2  not possible
(1,0)  = nr=2 nc=2  its is inf append to q dist=1+1=2
(0,-1) = nr=1 nc=1  its is inf append to q dist=1+1=2
(0,1)  = nr=1 nc=3  blocked

q=[(2,0),    (2,2),(1,1)]
r=0 c=3
(-1,0) - nr=-1 nc=3 X
(1,0)  - nr=1 nc=3 blocked
(0,-1) - nr=0 nc=2 already 0
(0,1)  - nr=0 nc=4 X

    0    1   2    3
0  inf  -1   0    1
1  2     2   1   -1 
2  1    -1   2  -1
3  0    -1   inf  inf

dist=2  q=[(2,0),    (2,2),(1,1)]
q=[(2,2),(1,1)]
r=2 c=0
(-1,0) - nr=1 nc=0 marked
(1,0)  - nr=3 nc=0 its 0 already
(0,-1) - nr=2 nc=-1 X
(0,1)  - nr=2 nc=1 blokced

    0    1   2    3
0  inf  -1   0    1
1  2     2   1   -1 
2  1    -1   2  -1
3  0    -1   inf  inf

q=[(2,2),(1,1)]
r=2 c=2 dist=2 
(-1,0) nr=1 nc=2 - visited
(1,0)  nr=3 nc=2 - its is inf append to q dist=2+1=3
(0,-1) nr=2 nc=1 - blocked
(0,1)  nr=2 nc=3 - blocked

q=[(1,1),  (3,2)]
r=1 c=1 dist =2  
(-1,0) nr=0 nc=0  its is inf append to q dist=2+1=3
(1,0)  nr=2 nc=1  blocked
(0,-1) nr=1 nc=0  visited
(0,1)  nr=1 nc=2  visted

    0    1   2    3
0  3    -1   0    1
1  2     2   1   -1 
2  1    -1   2  -1
3  0    -1   3  inf

q=[(3,2),(0,0)]
r=3 c=2 dist=3
(-1,0) nr=2 nc=2 visited
(1,0)  nr=4 nc=2 X
(0,-1) nr=3 nc=1 blocked
(0,1)  nr=3 nc=3 its is inf append to q dist=3+1=4

    0    1   2    3
0  3    -1   0    1
1  2     2   1   -1 
2  1    -1   2   -1
3  0    -1   3   4

q=[(0,0)   (3,3)]

next pop (0,0)-- already done
next pop (3,3) -- already done

'''