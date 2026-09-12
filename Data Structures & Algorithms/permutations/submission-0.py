class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        res = []

        visited = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                res.append(list(permutation))

            for i in range(len(nums)):
                if not visited[i]:
                    permutation.append(nums[i])
                    visited[i] = True

                    backtrack()

                    permutation.pop()
                    visited[i] = False

        backtrack()
        return res


"""
tc: O(n. n!)
sc: O(n. n!)
goal - all possible permutations 

[1,2,3]

[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

bruteforce: loop over i - 0, len(nums)
                loop over j=0 to len(nums)   
                    if i==j: skip
                    loop over k= 0 to len(nums)
                        if k==i or k==j: skip
                        append to res nums[i],nums[j],nums[k]

optimal approach: Backtracking/Recursion

res = []
permutations =[]
visited= [F F F]

backtrack()
    i=0 
        visited[0]=F yes
        permutations = [1]
        visited[0]=T [T F F]
        backtrack()
            i=0
                visited[0]=T skip
            i=1
                visited[1]= F
                permutations = [1,2]
                visited[1]=T [T T F]
                backtrack()
                    i=0 skip 
                    i=1 skip
                    i=2 
                        visited[2]=F
                        permutations = [1,2,3]
                        visited[2]=T [T T T]
                        backtrack()
                            len(perm)==len(nums): res=[[1,2,3]]
                permutations = [1,2]
                visited[2]=F [T T F]
                
        permutations = [1]
        visited[1]=F [T F F]
            i=2
                permutions=[1,3]
                visited= [T F T]
                backtrack()
                    loop from 0,1,2
                    i=0 skip
                    i=1 
                        permutation=[1,3,2]
                        visited=[T T T]
                        backtrack()
                            3==3? yes  res=[[1,2,3], [1,3,2]]
                            i=0 ,1,2,--skip
                    i=2 skip
                permutation=[1,3]
                visited=[T F T]
        permutation=[1]
        visited=[T F F]

    permutation=[]
    visited=[F F F]        
    i=1
        i=0 
            permutation=[2] visited=[F T F]
            backtrack()
                i=0
                    permutation=[2,1] visited=[T T F]
                    backtrack()
                        i=0 skip
                        i=1 skip
                        i=2 
                            permutation=[2,1,3] visited=[T T T]
                            backtrack()
                                3==3? yes res=[[1,2,3], [1,3,2],[2,1,3]]
                                i=0,i=1,i=2 skip
                    permutation=[2,1] visited=[T T F]
            permutation=[2] visited=[F T F]
                i=1 skip
                i=2
                    permutation=[2,3] visited=[F T T]
                    backtrack()
                        i=0 
                            permutation=[2,3,1] visited=[T T T]
                            backtrack()
                                3==3 yes res=[[1,2,3], [1,3,2],[2,1,3,[2,3,1]]]
                        i=1 skip
                        i=2 skip
                    permutation=[2,3] visited=[F T T]
            i=1 skip
            i=2 skip
        permutation=[2] visited=[F T F]

        permutation=[] visited=[F F F]

    i=2
            and so on....

Final res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    

"""
