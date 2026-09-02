class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited= set()

        def dfs(node, parent):
            
            visited.add(node)
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor,node):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n


'''
Tc: O(V + E)
Sc: O(V + E)
valid tree -  no cycle and every node should be connected

approach: cycle detection dfs

1. build adj list
2. run dfs starting from 0 node and no parent dfs(current_node, parent_node)
3. have visited to check if all nodes are visited
4. check if nodes are visited but not parent node
5. if no cycle and all nodes visited - return True else false


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

adj=[[1,2,3],[0,4],[0],[0],[1]]
visited = {}

dfs(0,None)
    0 in visited? no visited = {0}
    check its adj [1,2,3]
    dfs(1,0)
        1 in visited? no visited= {0,1}
        check if adj [0,4]
            check if 0 is visited? yes
            skip it
            check if 4 is visited??? no {0,1,4}
                chech it adj= [1] and 1==parent? 1==1? yes
                skip it
           
    dfs(2,0)
        2 in visited? no  visited= {0,1,4,2}
        check its adj [0]
            0==0 yes skip it
    dfs(3,0)
        3 in visited? no visited= {0,1,4,2,3}
        check its adj [0]
            0==0? skip it

return True

--------------------------------------------------------------------------------------------------
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

adj= [[1],[0,2,3,4],[1,3],[1,2],[1]]
visited= {}

dfs(0,None)
    0 in visited? no visited= {0}
    check its adj [1]
        1 in visited no?
        dfs(1,0)
            check if 1 in visited?no visited= {0,1}
            check its adj= [0,2,3,4]
            0 -- 0 in visited? yes skip it
            2 -- 2 in visited?no
            dfs(2,1)
                2 in visited? no visited = {0,1,2}
                check its adj [1,3]
                1==1? yes skip it
                3==1 no and not in visited
                    dfs(3,1)
                        3 in visited? no visited= {0,1,2,3}
                        check its adj [1,2]
                        1==1 yes skip it
                        2 != parent AND 2 is already visited -> cycle 
                        return false

false

'''