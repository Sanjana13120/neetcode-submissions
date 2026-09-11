class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combinations = []
        res = []

        def backtrack(start):
            res.append(list(combinations))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                combinations.append(nums[i])
                backtrack(i + 1)
                combinations.pop()

        backtrack(0)
        return res


"""
tc: O(n . 2**n)
sc: O(n)

Input: nums = [1,2,1]

goal- find all subset with duplicates

[[],[1],[2],[1,2],[1,1],[1,2,1]]

[1,2] and [2,1] are same... we should not generate [2,1]

combinations = []
res= []

sort the nums to avoid duplicates -- [1,1,2]

backtrack(0)
    res=[[]]
    for i=0,1,2
    i=0
        combinations=[1]
        backtrack(1)
            res=[[],[1]]
            for i=1,2
            i=1
                combinations=[1,1]
                backtrack(2)
                    res=[[],[1],[1,1]]
                    combinations=[1,1,2]
                    backtrack(3)
                        res=[[],[1],[1,1],[1,1,2]]
                        i=3X
                combinations=[1,1]
            combination=[1]
            i=2
                combinations=[1,2]
                backtrack(3)
                    res=[[],[1],[1,1],[1,1,2],[1,2]]
                    for i=3 X
            combinations=[1]
    combinations=[]
    i=1
        i>start? 1>0? yes and nums[i]==nums[i-1]-->nums[1]==nums[0]?yes
        skip this
    i=2
        combinations=[2]
        backtrack(3)
            res=[[],[1],[1,1],[1,1,2],[1,2],[2]]
            i=3 X

    combinations=[]


res=[[],[1],[1,1],[1,1,2],[1,2],[2]]



"""
