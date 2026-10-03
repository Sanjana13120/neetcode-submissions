class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0
        maxlen = 0

        for num in seen:
            if num - 1 not in seen:
                count = 1
                curr = num

                while curr + 1 in seen:
                    count += 1
                    curr += 1

                maxlen = max(maxlen, count)

        return maxlen


"""
tc: O(n)
sc: O(n)

goal - length of longest consecutive sequence of elements

approach 1:
1. sort the ele and convert to set to remove duplicates - O(nlogn)

approach 2: (optimal)
1. convert to set
2. for each num check if num-1 exist in seen. 
        if num-1 doesnt exist in seen then num is my start of the sequence
            from that num, keep checking num+1 and count    

Input: nums = [2,20,4,10,3,4,5]

seen = (2 20 4 10 3 5)

num=2-> 2-1=1 in seen? no so 2 is my start count=1
            2+1=3 in seen? yes count=2
            3+1=4 in seen? yes count=3
            4+1=5 in seen? yes count=4
            5+1=6 in seen? no
            maxlen=4

num=20 20-1=19 in seen? no so 20 is my start count=1
            20+1 in seen?no
            maxlen=max(4,1)=4

num=4 4-1 in seen? yes so 4 not my start
num=10 10-1=9 in seen? no count=1
        10+1 in seen?no

num=3 3-1 in seen? yes so 3 not my start

num=4 4-1 in seen? yes so 4 not mystart

num=5 5-1 n seen? yes so5 not my start


---------------------------------------------------------------------------------------------

Input: nums = [0,3,2,5,4,6,1,1]

seen = (0 3 2 5 4 6 1)

num=0 0-1=-1 in seen? no 0 is my start count=1
        0+1 in seen? yes count=2
        1+1 in seen? yes count=3
        2+1 in seen? yes count=4
        3+1 in seen? yes count=5
        4+1 in seen? yes count=6
        5+1 in seen? yes count=7
        6+1 in seen? no
        maxlen=max(0,7)=7

num=3 3-1 in seen? yes
num=2 2-1 in seen? yes
num=5 5-1 in seen? yes
num=4 4-1 in seen? yes
num=6 6-1 in seen? yes
num=1 1-1 in seen? yes

so finaly return maxlen=7
"""
