"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        copy={}
        def dfs(node):
        
            if node in copy:
                return copy[node]

            clone=Node(node.val)
            copy[node] = clone
            
            for neighbor in node.neighbors:
                neighbor_clone = dfs(neighbor)
                clone.neighbors.append(neighbor_clone)

            return clone


        return dfs(node)


'''
tc: O(V+E)
sc: O(V)

we have to do a deep copy
dfs approach

we first create a copy of nodes
copy = {1: 1', 2:2', 3:3'}

1' = [2']
2' = [1',3']
3  = [2']

loop over the node.neigbours 
    append to copyAdjList

eg : adj = [[2],[1,3],[2]]

1 - [2]
2 - [1,3]
3 - [2]

copy = {}
visit 1 create 1'
copy = {1:1'}
now neighbours of 1 is [2]
    is [2] cloned -- no so create 2' --> copy = {1:1',2:2'} -  1'=[]
    1'=[2']
    return back

    visit 2
    copy = {1:1',2:2'}
    neighbours of 2 are [1,3]
        [1] already cloned  --reuse-- 2'= [1']
        [3] not cloned   -- create 3' --> copy = {1:1',2:2',3:3'} - 2'=[1',3']
        return to 1
        
        visit 3
        copy = {1:1',2:2',3:3'}
        neighbours of 3 is [2] 
        [2] already cloned -- 3'=[2']
        return to 2



    




'''