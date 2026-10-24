class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval) 
                res.extend(intervals[i:])
                return res

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res 


"""
TC = O(n)
SC = O(n)

goal - Return intervals after adding newInterval.

intervals = [start, end] ....

we have to insert newinterval in intervals 
    if overlap - take min and max
    if not simply insert 

it should be in sorted order only

approach:

1. compare the end of intervals with start of newinterval
    if intervals[i][1] < newInterval[0] 
        then append intervals[i] to res

2. compare start of intervals with end of newInterval
    if intervals[i][0] > newInterval[1]
        then append newInterval

3. otherwise they ovelap so find min(newInterval[0], intervals[i][0]) and max(newInterval[1],  intervals[i][1])

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

first [1,3]
3<2? no
1>5? no

so min(2,1)=1 and max(5,3)=5

newInterval = [1,5]

next compare [4,6] and [1,5]

6<1? no
4>5? no

so min(1,4)=1 and max(5,6)=6

newInterval = [1,6]

res= [1,6]

---------------------------------------------------------------------------------------------------------
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

compare [1,2] with [6,7]

2<6? yes so res=[1,2]

compare [3,5] with [6,7]

5<6? yed res=[[1,2], [3,5]]

compate [9,10] with [6,7]

10<6? no
9>7? yes  res=[[1,2], [3,5], [6,7], [9,10]]



"""
