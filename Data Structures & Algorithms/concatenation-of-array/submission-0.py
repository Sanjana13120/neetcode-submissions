class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums*2
        return nums + nums


# tc: O(n) -- copies the elements into a new list of length 
# sc: O(n) -- reates a new list containing 2n elements.
