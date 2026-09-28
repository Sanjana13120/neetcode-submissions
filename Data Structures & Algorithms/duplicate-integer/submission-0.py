class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq = Counter(nums)

        # for num, count in freq.items():
        #     if count>1:
        #         return True
        
        # return False

# tc: O(n)
# sc: O(n)

        # hashset

        seen=set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)

        return False

        # tc: O(n)
        # sc: O(n)


