"""
Pattern: Multi-source BFS

Multiple rotten oranges spread simultaneously. So put all of them in the queue initially.

Important BFS trick: for _ in range(len(q)):

1. Count fresh oranges
2. Put ALL rotten oranges into queue
3. BFS level = 1 minute
4. For each rotten orange:
   → check 4 directions
   → if fresh:
      - make it rotten
      - fresh -= 1
      - add to queue
5. If fresh == 0 → return minutes
6. Else → return -1


"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes=0
        fresh=0
        directions={(-1,0),(1,0),(0,-1),(0,1)}
        rows=len(grid)
        cols=len(grid[0])

        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i,j])

        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    newrow=r+dr
                    newcol=c+dc

                    if 0<=newrow<rows and 0<=newcol<cols and grid[newrow][newcol]==1:
                        fresh-=1
                        grid[newrow][newcol]=2
                        q.append([newrow,newcol])

            minutes+=1

        return minutes if fresh==0 else -1

'''
tc: O(r*c)
sc: O(r*c)

  0 1 2
0 1 1 0
1 0 1 1
2 0 1 2

bfs- approach

q=[(2,2)] - store all rotten fruit grid[i][j]==2
fresh = 5 - count of fresh fruits grid[i][j]==1

directions = {(-1,0),(1,0),(0,-1),(0,1)}
minutes=0 
chekc until q is empty and fresh>0
    loop over (len(q))
        r=2 c=1 and check top left bottom and right wheter it is fresh grid[i][j]==1
            if yes decrease fresh-=1  and mark that as rotten and append the new r,c to the queue

    increase the minutes

rows=3 cols=3
min=0
q=[(2,2)] , r=2 c=2
(-1,0) nr=1 nc=2 grid[1][2]==1? yes fresh=4, rotten it and append to q
(1,0) nr=3 nc=1 not possible
(0,-1) nr=2 nc=1 1==1? yes fresh=3  rotten it and append to q
(0,1) nr=2 nc=3 not possible

q=[(1,2),(2,1)]

  0 1 2
0 1 1 0
1 0 1 2
2 0 2 2

min=1
q=[(2,1)]  r=1 c=2
(-1,0) nr=0 c=2 empty blocked
(1,0) nr=2 nc=2 already rotten
(0,-1) nr=1 nc=1 1==1? yes fresh=2 rotten it and append to q
(0,1) nr=1 nc=3 not possible

r=2 c=1

(-1,0) nr=1 nc=1 alreadyt rotten
(1,0) nr=3 nc=1 X
(0,-1) nr=2 nc=0 blocked
(0,1) nr=2 nc=2  already rotten

  0 1 2
0 1 1 0
1 0 2 2
2 0 2 2

min=3
q=[(1,1)]
r=1 c=1  -- q=[]

(-1,0) nr=0 nc=1 1==1? yes fresh=1 rotten it and append to q
(1,0)  nr=2 nc=1 alredy rotten
(0,-1) nr=1 nc=0 blocked
(0,1)  nr=1 nc=2 alreay rotten

  0 1 2
0 1 2 0
1 0 2 2
2 0 2 2

min=4

q=[[0,1]]
r=0 c=1 q=[]
(-1,0) nr=-1 nc=1 X
(1,0) nr=1 nc=1 already rotten
(0,-1) nr=0 nc=0 1==1? yes fresh=0 rotten it and append to q
(0,1) nr=0 nc=2 blocked

  0 1 2
0 2 2 0
1 0 2 2
2 0 2 2

q=[(0,0)] 

q is not empty but fresh==0! so come out of loop

return min=4 

----------------------------------------------------------------------------------------
   0 1 2
0  1 0 1
1  0 2 0
2  1 0 1


directions = {(-1,0),(1,0),(0,-1),(0,1)}
minutes=0 
fresh=4
q=[(1,1)]

min=0 and q=[(1,1)] 
r=1 c=1 
(-1,0) nr=0 nc=1  blocked
(1,0) nr=2 nc=1 blocked
(0,-1) nr=1 c=0 blocked
(0,1) nr=1 nc=2 blocked

   0 1 2
0  1 0 1
1  0 2 0
2  1 0 1

q=[] and fresh>0 yes

return min if fresh==0 else -1

output is -1

'''