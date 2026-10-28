class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True


"""
tc: O(nlogn)
sc: O(n)

goal - determine if a person could add all meetings to their schedule without any conflicts

Approach: Sorting + Linear Scan

The meetings must not overlap.

If any two meetings overlap → return False.
If no meetings overlap → return True.

1. Sort all intervals by their start time.
2. Compare consecutive meetings:
    Check whether the previous meeting's end time is greater than the next meeting's start time.
    If prev.end > next.start, return False.
3. If no overlapping meetings are found, return True.

--------------------------------------------------------------------------------------

Input: intervals = [(0,30),(5,10),(15,20)]

compare (0,30) and (5,10)

30>5 return False

--------------------------------------------------------------------------------------

Input: intervals = [(5,8),(9,15)]

compare (5,8) and (9,15)

8>9? no

return True

"""
