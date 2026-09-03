class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()

        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor in visited:
                    continue

                dfs(neighbor)


        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)

        return count
                
'''
tc: O(V+E)
sc: O(V+E)
n nodes and edges 0 - n-1
edges[i]=[a,b]

find the no of connected components

Approach: DFS

1. build adj list
2. visited = set() and count=0
3. loop through every node
4. if node is not visited
    count+=1
    run the dfs and mark as visited
    then check its neighbor and if already visited skip
    else run the dfs

n = 5, edges = [[0,1],[1,2],[3,4]]

adj=[[1],[0,2],[1],[4],[3]]
count=0

for i -- 0,1,2,3,4

count=1
dfs(0) 
    visited={0}
    check its adj - [1]
    1 is not visited
    dfs(1)
        visited={0,1}
        check its adj [0,2]
        0 already visited - skip it
        2 not visited
        dfs(2)
            visited ={0,1,2}
            check its adj- [1]
            1 is visited - skip it


dfs(1)- already visited
dfs(2)-- already visited

count=2
dfs(3)
    visited={0,1,2,3}
    check its adj- [4]
    4 not visited
    dfs(4)
        visited={0,1,2,3,4}
        check its adj=[3]
        3 already visited - skip it

return count=2

'''