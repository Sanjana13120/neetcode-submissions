class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []

        for num, count in freq[:k]:
            res.append(num)

        return res


"""

goal - return top k most freq elements

Input: nums = [1,2,2,3,3,3], k = 2

1:1 2:2 3:3
k>=2? is 2 and 3

res= [2,3]

approch 1: hashmap

1. count the freq using counter.
2. sort the freq desc

tc: O(nlogn)
sc: O(n)


"""
