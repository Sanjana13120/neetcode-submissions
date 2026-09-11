class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        res = []

        def backtrack(start):
            res.append(list(combinations))

            for i in range(start,len(nums)):
                combinations.append(nums[i])

                backtrack(i+1)

                combinations.pop()

        backtrack(0)
        return res
        
'''
tc: O(n)*O(2^n) = O(n 2^n)
sc: O(n) - recursion stack + combinations.
    O(2^n) - output res


[1,2,3]

goal - generate all possible subset without any duplicates

output - [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

Approach: Backtracking/Recursion

combination = []
res=[]

backtrack(0)
    res=[[]]

    loop over nums from 0,1,2
        i=0
            combinations= [1]
            backtrack(1)
                res= [[], [1]]
                loop over 1,2
                    i=1
                        combinations=[[1,2]]
                        backtrack(2)
                            res=[[],[1],[1,2]]
                            loop over i=2
                                combinations = [1,2,3]
                                    backtrack(3)
                                        res=[[],[1],[1,2],[1,2,3]]
                                        loop over 3 X
                                    combinations=[1,2]
                            combinations=[1]
                    i=2
                        combinations=[1,3]
                        backtrack(3)
                            res=[[],[1],[1,2],[1,2,3],[1,3]]
                            loop over 3,3 X
                        combinations=[1]
            combinations=[]

        i=1
            combinations=[2] 
            backtrack(2)
                res=[[],[1],[1,2],[1,2,3],[1,3],[2]]
                loop over 2
                combinations=[2,3]
                backtrack(3)
                    res=[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3]]
                    loop over 3 x
                combinations=[2]
            combinations=[]

        i=2
            combinations=[3]
            backtrack(3)
                res=[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
                loop over 3 X
            combinations=[]

res=[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]






'''