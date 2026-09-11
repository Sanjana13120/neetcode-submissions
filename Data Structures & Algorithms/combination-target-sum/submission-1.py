class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        res = []
        nums.sort()
        
        def backtrack(start,target):
            if target == 0:
                res.append(list(combinations))
                return

            for i in range(start,len(nums)):
                if nums[i] > target:
                    break

                combinations.append(nums[i])

                backtrack(i,target-nums[i])

                combinations.pop()

        backtrack(0,target)
        return res
        

'''
tc: O(n^T)
sc: O(T)
T- target

nums = [2,5,6,9]  target = 9

combinations=[]
res=[]

backtrack(0,9)
    loop over 0 to len(nums)- 0,1,2,3
    i=0
        combinations= [2]
        backtrack(0,7)
            loop over 0,1,2,3
            i=0
                combinations=[2,2]
                backtrack(0,5)
                    loop over 0,1,2,3
                    i=0
                        combinations=[2,2,2]
                        backtrack(0,3)
                        loop over 0,1,2,3
                        i=0 
                            combinations=[2,2,2,2]
                            backtrack(0,1)
                            i=0
                                2>1? yes so break
                        combinations=[2,2,2]
                        i=1
                            5>3 yes break
                combinationsn=[2,2]
                    i=1
                        5>5? no
                        combinations=[2,2,5]
                        backtrack(1,0)
                            target==0?0==0? yes
                            res=[[2,2,5]]
                            return
                combinations=[2,2]
                    i=2
                        6>5 yes break
                    i=3
                        9>5 yes break
            combinations=[2]
            i=1,2,3 aqnd so on
    i=1 x
    i=2 x
    i=3 
        combinations=[9]
        backtrack(3,0)
            0==0? yes
            res=[[2,2,5],[9]]






'''