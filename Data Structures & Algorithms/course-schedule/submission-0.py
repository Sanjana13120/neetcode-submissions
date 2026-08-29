class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states=[0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[a].append(b)

        def dfs(course):
            if states[course]==1:
                return False
            if states[course]==2:
                return True

            states[course]=1

            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False

            states[course]=2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

'''
tc: O(V+E)
sc: O(V+E)

Approach: cycle detection DFS in directd graph
to complete course 1 we have to complete course 0 for [1,0]  : 0 -> 1

You can finish all courses only if there is no cycle in this directed graph.

we have 3 states here
0-> not visited
1-> currently exploring
2-> explored

0-1-0  -- so this is a cycle hence we cannot complete all course

1. create adj list
2. we have 3 states
3. run dfs for unvisited node
4. if we reach node with state 1--> cycle found - return False
   if we reach node with state 2--> skip it
   if we reach node with state 0--> mark as 1 and run dfs
5. After visiting neighbors mark as 2
6. no cycle found - return True

----------------------------------------------------------------------------------------------------------
Input: numCourses = 2, prerequisites = [[0,1]]

adj= [[1],[]]
states= [0,0]
dfs(0)
    check state[0] is 1 or 2 or 0? it is 0 so
        states[0]=1  (states=[1,0])
    check for neighbors in adj. it is 1
        dfs(1)
        check state[1] is 1 or 2 or 0? it is 0 so
            states[1]=1  (states=[1,1])
        check for neigbors in adj, nothing 
        so mark states[1]=2
    mark states[0]=2

return True

----------------------------------------------------------------------------------------------------------
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
0->1->0

adj[0]=[1]
adj[1]=[0]

states= [0,0]
dfs(0)
    check state[0] is 1 or 2 or 0? it is 0 so
        states[0]=1    (states=[1,0])
    check for neighbors in adj. it is 1
        dfs(1)
        check state[1] is 1 or 2 or 0? it is 0 so
            states[1]=1  (states=[1,1])
        check for neigbors in adj, its is 0
            dfs(0)  
            check state[0] is 1 or 2 or 0? it is 1--> cycle found return false



'''