class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        edges=[]
        parent = [i for i in range(n)]

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            
            parent[root_v] = root_u
            return True

        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges.append((dist,i,j))
        edges.sort()
        
        merge_count = min_cost = 0

        for dist, u, v in edges:
            if union(u,v):
                min_cost+=dist
                merge_count+=1

        return min_cost


'''
tc: O(n² log n)
sc: O(n²)
Building all edges:       O(n²)
Sorting E = O(n²):        O(n² log n)
DSU processing:           O(n² · α(n)) ≈ O(n²)

Overall:                  O(n² log n)

givrn points where the  cost of connecting two points is the manhattan distance between the two points

The goal is: Connect all points with the minimum possible total cost.

The cost between two points is Manhattan distance.

Approach - Kruskal Algorithm 

Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

1. First build the edges from the given points. Generate every possible edge → calculate its Manhattan cost → 
    store (cost, i, j)
A = [0,0]
B = [2,2]
C = [3,3]
D = [2,4]
E = [4,2]

now build the graph: AB, AC, AD, AE, BC, BD, BE, CD, CE, DE
EG: AB = [0,0] and [2,2] -- (0-2)+(0-2)=4

(4, A, B)
(6, A, C)
(6, A, D)
(6, A, E)

(2, B, C)
(2, B, D)
(2, B, E)

(2, C, D)
(2, C, E)

(4, D, E)

[(4, 0, 1), (6, 0, 2), (6, 0, 3), (6, 0, 4), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 3), (2, 2, 4), (4, 3, 4)]

2. Sort the edges by cost. 
[(2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 3), (2, 2, 4), (4, 0, 1), (4, 3, 4), (6, 0, 2), (6, 0, 3), (6, 0, 4)]

3. DSU the edges
4. Take the cheapest edge.
5. find() both endpoints.
6. if roots are different:
    merge them
    add the cost
    increase merge count


parent = [0 1 2 3 4],   mergecount=0,   cost=0
Process (2,1,2)
1 and 2 are not connected
so parent = [0 1 1 3 4]
mergecount = 1
cost = 2

Process (2,1,3)
1 and 3 are not connected
parent = [0 1 1 1 4]
mergecount = 2
cost = 2+2 = 4

process(2,1,4)
1 and 4 are not connected
parent = [0 1 1 1 1]
mergecount = 3
cost = 4+2 = 6

process (2,2,3)
2 and 3 are connected? yes skip it

process (2,2,4)
2 and 4 are connected? yes skip it

process (4,0,1)
0 and 1 not connected
parent = [1 1 1 1 1]
mergecount = 4
cost = 6+4 = 10

mergecount==n-1 and all are visited so 
return cost=10






'''