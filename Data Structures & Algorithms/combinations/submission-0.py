class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        res= []

        def backtrack(start):

            if len(combinations) == k:
                res.append(list(combinations))
                return
            
            for i in range(start,n+1):
                combinations.append(i)
                backtrack(i+1)
                combinations.pop()

        backtrack(1)
        return res

'''
tc: O(k . C(n,k))
sc: O(k)

goal: genetate all possible combinations of k size
n=3 k=2
[1,2], [1,3],[2,3]

n=3 k=3
[1,2,3]

n=4 k=2
[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]

n=3 k=2

combinations=[]
res=[]
backtrack(1)
    for loop 1,2,3
    i=1
        combinations=[1]
        backtrack(2)
            for loop i=2,3
            i=2
                combinations=[1,2]
                backtrack(3)
                    len(comb)==k: yes so res=[[1,2]]
                combinations=[1]
            i=3
                combinations=[1,3]
                backtrack(3)
                    2==2? yes res=[[1,2],[1,3]]
                combinations=[1]
    combinations=[]
    i=2
        for loop 2,3
            combinations=[2]
            backtrack(3)
                i=3
                    combinations=[2,3]
                    backtrack(4)
                        2==2 yes res=[[1,2],[1,3],[2,3]]
            combinations=[2]
    combinations=[]
    i=3
        for loop 3,3 x

res=[[1,2],[1,3],[2,3]]
                

'''