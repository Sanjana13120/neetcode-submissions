class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        nums.sort()
        res = []
        visited = [False] * len(nums)

        def backtrack():
            if len(permutations) == len(nums):
                res.append(list(permutations))
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                if not visited[i]:
                    permutations.append(nums[i])
                    visited[i] = True

                    backtrack()

                    permutations.pop()
                    visited[i] = False

        backtrack()
        return res


"""
tc: O(n.n!)
sc: O(n.n!) including res
    O(n) excluding output
    
we need to sort the nums
[1 1 2]

[1 1 2], [1 2 1] [2 1 1]

permutation = []
visited= [F F F]
backtrack() 
    i=0
        permutation=[1]
        visited= [T F F]
        backtrack()
            i=0 visited
            i=1 
                permutation=[1,1]
                visited= [T T F]
                backtrack()
                    i=0 visited
                    i=1 visited
                    i=2 
                        permutation=[1,1,2]
                        visited= [T T T]
                        backtrack()
                            len(perm)==len(nums)? 3==3?yes res=[[1,1,2]]
                        undo 2
                        permutation=[1,1]
                        visited= [T T F]
                    return
            undo 1
            permutation=[1]
            visited= [T F F]
            i=2
                permutation=[1,2]
                visited= [T F T]
                backtrack()
                    i=0 skip
                    i=1
                        permutation=[1,2,1]
                        visited= [T T T]
                        backtrack()
                            3==3? yes res=[[1,1,2],[1,2,1]]
                        undo 1
                        permutation=[1,2]
                        visited= [T F T]
                    i=2 skip
                undo 2
                permutation=[1]
                visited= [T F F]
        undo 1
        permuataion=[]
        visited=[F F F]
    i=1
        nums[1]==nums[0] and not visited[0]? 1==1? yes and !F=T-- T&T skip
    i=2
        permuataion=[2]
        visited=[F F T]
        backtrack()
            i=0
                permuataion=[2,1]
                visited=[T F T]
                backtrack()
                    i=0 skip
                    i=1 nums[1]==nums[0] and !T ==F 
                        permuataion=[2,1,1]
                    visited=[T T T]
                    backtrack()
                        3==3? res=[[1,1,2],[1,2,1],[2,1,1]]
                        return
                    undo 1
                undo 1
            perm=[2]
            visited=[F F T]
            i=1
                1==1 and !F=T -- t skip
            i=2 skip
    undo 2
    perm=[]
    visited=[F F F]                      



"""
