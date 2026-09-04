class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        size = [1]*(len(edges)+1)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        
        for u,v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return [u,v]

            if size[root_u] < size[root_v]:
                root_u,root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] += size[root_v]

'''
tc: TC: O(E α(V)) ≈ O(E)
sc: O(V)
edges = [[1,2],[1,3],[3,4],[2,4]]

parent = [0 1 2 3 4]

[1,2]
find(1) --> 1
find(2) --> 2

1!=2 so merge them
parent[2]=1

parent = [0 1 1 3 4]

[1,3]
find(1)-->1
find(3)-->3
1!=3 so merge them--> parent[3]=1

parent = [0 1 1 1 4]

[3,4]
find(3)-->1
find(4)-->4
1!=4 so merge them --> parent[4]=3

parent = [0 1 1 1 3]

[2,4]
find(2)-->1
find(4)-->find(3)-1 root=1
parent[4]=1

parent = [0 1 1 1 1]

1==1? yes

so ans is [2,4]


'''