class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = float("-inf")
        count = 0

        for start, end in intervals:
            if start >= prev:
                count += 1
                prev = end

        return len(intervals) - count


"""
tc: O(nlogn)
sc: O(1) or O(n) depending on sorting

goal -  return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,4],[1,4]]

1---2---3---4
to make this interval non-overlapping [1,4] overlaps so remove [1,4]

basically non-overlapping -> Two intervals are non-overlapping if the current interval's start is greater than or equal to the end of the previous kept interval.

approach: Greedy

1. Sort intervals by end time in ascending order.
2. Initialize:
    prev = float("-inf")
    count = 0 (number of intervals kept)
3. Iterate through each interval [start, end]:
    If start >= prev:
        Keep the interval.
        Increment count.
        Update prev = end.
    If start < prev:
        The interval overlaps with the previous kept interval.
        Skip it.
        Do not update count or prev.
4. Return len(intervals) - count.

-------------------------------------------------------------------------------------------------------------------

[1,2] [1,4] [2,4]

count = 0
start = 1  end = 2 prev = -inf
if 1>=-inf? yes
    count=1
    prev = 2

start=1 end= 4 prev = 2
if 1>=2? no

start=2 end=4 prev=2
2>=2? yes
    count=2
    prev =4

return len(intervals) - count = 3-2=1

-------------------------------------------------------------------------------------------------------------------

Input: intervals = [[1,2],[2,4]]
prev= -inf

start=1 end=2 
1>=-inf? yes count=1 prev=2

start=2 end=4 prev=2
2>=2? yes count=2 prev=4

len(intervals) - count = 2-2=0

-------------------------------------------------------------------------------------------------------------------
intervals = [[1, 100], [2, 3], [3, 4]]

[2,3], [3,4], [1,100]

start=2 end=3 prev=-inf
2>=-inf yes count=1 prev=3

start=3 end=4 prev=3
3>=3> yes count=2 prev=4

start=1 end=100 prev=4
1>=4? no

len(intervals)-count = 3-2=1

"""
