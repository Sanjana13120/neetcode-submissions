"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        rooms = 0

        intervals.sort(key=lambda x:x.start)
        

        for i in range(len(intervals)):

            while heap and heap[0]<=intervals[i].start:
                heapq.heappop(heap)

            heapq.heappush(heap,intervals[i].end)

            rooms = max(rooms, len(heap))

        return rooms
        

'''
tc: O(nlogn)
sC: O(n)

goal -  find the minimum number of rooms required to schedule all meetings without any conflicts.

Approach:
overlapping one room non overlapping anohter room?

1. sort by start time
2. Initialize an empty min-heap.
3. For each meeting:
        While the heap is not empty and the earliest end time is less than or equal to the current start time, pop it.
        Push the current meeting's end time.
        Update the maximum heap size.
4. return len(heap)

Input: intervals = [(0,40),(5,10),(15,20)]
heap = []

process (0,40)
heap = [40]

process (5,10)
40<=5? no
heap = [10 40]

process (15,20)
10<=15? yes so pop heap = [40]
heap= [20 40]

return len(heap) = 2


'''