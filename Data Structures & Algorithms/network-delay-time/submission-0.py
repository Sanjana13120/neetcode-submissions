import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap=[(0,k)]
        ans=0
        count=0
        visited=[False]*(n+1)

        adj = [[] for _ in range(n+1)]

        for source,dest,time in times:
            adj[source].append((dest, time))

        while heap:
            curr_time, node = heapq.heappop(heap)

            if visited[node]:
                continue

            visited[node] = True
            count+=1
            ans=max(ans,curr_time)

            for neighbor, edge_time in adj[node]:
                new_time = curr_time + edge_time
                heapq.heappush(heap,(new_time, neighbor))

        return ans if count==n else -1


'''
tc: O(ElogV)
sc: O(E+V)
 times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

from k--> n what is the min time 

1-> 4 = 4
1-> 2 -> 3 = 3
so ans is 3

Approach: dijikstra

we build min heap heap = [(0,k)] -(time, node)

next find the adjlist = [[],[(2,1), (4,4)], [(3,1)], [(4,1)], []]
adj [1] = [(2,1), [4,4]]
adj [2] = [(3,1)]
adj [3] = [(4,1)]
adj [4] = []

visited = [F F F F F]

until heap is empty
    pop smallest node
    visit node, Skip if visited 
    Mark visited
    check neighbors
    find new_time =curr_time+edge_time
    Push neighbors with new_time
    count == n ? ans : -1

heap=[0,1]
ans=0 count=0

curr_time=0 node=1  heap=[]
visited = [F T F F F]
ans=0 count=1
adj of 1 is [(2,1), [4,4]]
    process (2,1) --> new_time=0+1=1 --> heap = [(1,2)]
    process (4,4) --> new_time=0+4=4 -->heap = [(1,2), (4,4)]

curr_time=1 node=2  heap=[(4,4)]
visited = [F T T F F]
ans=1 count=2
adj of 2 is [(3,1)]
    process (3,1)--> new_time=1+1=2 --> heap=[(2,3),(4,4)]

curr_time=2 node=3  heap=[(4,4)]
visited = [F T T T F]
ans=2 count=3
adj of 3 is [(4,1)]
    proceess (4,1)--> new_time=2+1=3 --> heap= [(3,4),(4,4)]

curr_time=3 node=4  heap=[(4,4)]
visited = [F T T T T]
ans=3 count=4
adj of 4 is []

curr_time=4 node=4 heap=[]
visited = [F T T T T] skip

ans = 3

------------------------------------------------------------------------------

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

heap = [(0,2)]
adjlist = [[],[(2,1)],[(3,1)],[]]
adj of [1]= [(2,1)]
adj of [2]= [(3,1)]
adj of [3] =[]

visited= [F F F F]
ans=0 count=0

heap=[(0,2)]
curr_time=0 node=2 heap=[]
visited= [F F T F]
ans=0 count=1
adj of 2 is [(3,1)]
    process (3,1) --> newtime=0+1=1 heap=[(1,3)]

curr_time=1 node=3 heap=[]
visited= [F F T T]
ans=1 count=2
adj of 3 is [] 

ans=-1 -->if count==n else -1




'''