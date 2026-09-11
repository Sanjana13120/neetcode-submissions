class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        res = []

        candidates.sort()

        def backtrack(start, target):

            if target == 0:
                res.append(list(combinations))
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                combinations.append(candidates[i])

                backtrack(i + 1, target - candidates[i])

                combinations.pop()

        backtrack(0, target)
        return res

"""
tc: O(n · 2^n)
sc: O(n)

Input: candidates = [9,2,2,4,6,1,5], target = 8

Approach: backtracking/recursion

goal- generate all possible combination sum == target without any duplicates 

combinations = []
res = []

first sort -- [1,2,2,4,5,6,9]

backtrack(0,8)
    loop over i=0,1,2,3,4,5,6
    i=0
        combinations=[1]
        backtrack(1,7)
            loop over i=1,2,3,4,5,6
            i=1
                combinations=[1,2]
                backtrack(2,5)
                    loop over 2,3,4,5,6
                    i=2
                        combinations=[1,2,2]
                        backtrack(3,3)
                            i=3 4>3? yes break

                combinations=[1,2]
            i=2
                2>1 and nums[i]==nums[i-1] yes skip
            i=3 
                combinations=[1,2,4]
                backtrack(4,1)
                i=4 5>1 x

                combinations=[1,2]
            i=4
                combinations=[1,2,5]
                backtrack(5,0)
                    target==0? yes res=[[1,2,5]]
                combinations=[1,2]
            combinations=[1]
        combinations=[]
        i=1
            combinations=[2]
            backtrack(2,6)
                loop over i=2,3,4,5,6
                i=2
                    2>2 ? no combinations=[2,2]
                    backtrack(3,4)
                        i=3 combinations=[2,2,4]
                            backtrack(4,0) 
                                0==0? yes res=[[1,2,5],[2,2,4]]
            combinations=[2]
                i=3 X
                i=4 x
                i=5 combinations=[2,6]
                    backtrack(6,0) 
                        0==0? res=[[1,2,5],[2,2,4],[2,6]]

            combinations=[2]
        combinations=[]
        i=2 start=1 i=2 2>1 and 2==2? yes sp skip this

        i=3 and so on......

finally....
res=[[1,2,5],[2,2,4],[2,6]]

        

"""
