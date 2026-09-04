class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(len(edges)+1)]

        def dfs(node, target):
            if node==target:
                return True

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor in visited:
                    continue

                if dfs(neighbor,target):
                    return True

            return False

        for u,v in edges:
            visited = set()
            if dfs(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)

        

'''
tc: O(E* (V+E))
sc: O(V+E)

for Redundant Connection, since E = V:since E=V
tc: O(V²)
sc: O(V)

initially its a tree -- which has no cycle
but some edge got added to tree which make it cyclic

so we have to find the redudant edge which makes the graph cyclic

1. start with empty adj list and maintain visited=[False]
2. for each u,v --> run the dfs from u to v
    if i can already reach v from u-> redudant edge
    else add to adj list

Input: edges = [[1,2],[1,3],[3,4],[2,4]]

adj = [[],[],[],[],[]]
visited= set()

[1,2]

    dfs(1,2) 
        visited = {1}
        check its adj --> []
        so add u,v to adj list
    adj = [[],[2],[1],[],[]]

[1,3]
    dfs(1,3)
    visited = {1}
        check its adj --> [2]
        dfs(2,3)
            visited ={1,2}
            check its adj of 2 --[1]
            already visited-- skip
    adj = [[],[2,3],[1],[1],[]]

[3,4]
    dfs(3,4)
        viisted={3}
        check its adj[3]--[1]
        dfs(1,4)
            visited ={3,1}
            check its adj==[2,3]
            2 is visited?no
            dfs(2,4)
                visited={3,1,2}
                check its adj-[1] already visited skip
            3 is vsited? yes skip

    we dint reach 4 so adj = [[],[2,3],[1],[1,4],[3]]

[2,4]
    dfs(2,4)
        visited={2}
        check its adj--[1]
        1 is not visited? 
        dfs(1,4)
            visited={2,1}
            check its adj [2,3]
            2 is visited? yes skip it
            3 is visited?no
            dfs(3,4)
                visited={2,1,3}
                check its adj=[1,4]
                1 is viistef? yes skip it
                4 is not visited?
                dfs(4,4)
                    4==4? reachability return true

retun [2,4]





    

    
'''