class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        combinations = []
        self.res = 0

        def backtrack(start, curr_xor):
            self.res += curr_xor

            for i in range(start, len(nums)):
                combinations.append(nums[i])
                backtrack(i + 1, curr_xor ^ nums[i])
                combinations.pop()

        backtrack(0, 0)
        return self.res


"""
tc: O(2^n)
sc: O(n)

Input: nums = [2,4]
find all subset
[],[2],[4],[2,4]
0+2+4+6=12

bactrack(0,0)
    res=0
    loop i=0,1
    i=0
        combinations=[2]
        backtrack(1,2)
            res=2
            loop i=1
                combinations=[2,4]
                backtrack(2,6)
                    res=8
                    loop i=3 X
                combinations=[2]
    combinations=[]
    i=1
        combinations=[4]
        backtrack(2,4)
            res=12
            loop i=3 X
    combinations=[]


return res=12

"""
