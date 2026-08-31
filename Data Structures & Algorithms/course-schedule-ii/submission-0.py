class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[a].append(b)

        res=[]
        states=[0]*numCourses

        def dfs(course):
            if states[course]==1:
                return False

            if states[course]==2:
                return True

            states[course]=1

            for neighbors in adj[course]:
                if not dfs(neighbors):
                    return False

            states[course]=2
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res 



'''
tc: O(V+E)
sc: O(V+E)

Input: numCourses = 3, prerequisites = [[1,0]]

1-->0

adj[0]=[]
adj[1]=[0]
adj[2] = []

adj=[[],[1]]
states= [0,0,0]

dfs(0)
    states[0]=1  states=[1,0,0]
    check it adj - nothing
    states[0]=2    states=[2,0,0]
    return true

res=[0]
dfs(1)
    states[1]=1   states=[2,1,0]
    check its adj  --[0]
    dfs(0)
        states[0]=2==2
        return True
    states[1]=2   states=[2,2,0]
    return true

res=[0,1]

dfs(2)
    states[2]=1  states=[2,2,1]
    check its adj notjing
    states=[2]=2  states=[2,2,2]
    return true

res=[0,1,2]

if true return res else []

-----------------------------------------------------------------------------------------------
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

this forms a cycle
0-1-2-0

adj[0]=[1]
adj[1]=[2]
adj[2]=[0]

states=[0,0,0]

dfs(0)
    states[0]=1   states=[1,0,0]
    check its adj [1]
    dfs(1)
        states[1]=1   states=[1,1,0]
        check its adj [2]
        dfs(2)
            states[2]=1  states[1,1,1]
            check its adj[0]
            dfs(0)=1
                states[0]=1==1 
                return false
        return False
    return False

return false


'''