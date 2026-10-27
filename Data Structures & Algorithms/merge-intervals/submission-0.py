class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)

            else:
                merged.append([start, end])

        return merged


"""
tc: O(nlogn)
sc: O(n)

goal - merge all overlapping intervals and return non overlapping intervals arr

Approach: Sort + Merge

1. Sort intervals by their start value in ascending order.
2. Initialize merged with the first interval.
3. Iterate through the remaining intervals.
4. Compare the current interval's start with the end of the last merged interval.
5. If start <= merged[-1][1]: The intervals overlap. Update the last merged interval's end to max(merged[-1][1], end).
6. Otherwise: Append the current interval to merged.
7. Return merged.

-------------------------------------------------------------------------------------------------------------------

Input: intervals = [[1,3],[1,5],[6,7]]

merged = [[1,3]]

[1,5]
start = 1 end=5
1<=merged[-1][1]? --> 1<=3? yes 
    merged[-1][1] =max(5,3)=5
    so merged replace with [1,5]

[6,7]
start= 6 end=7
6<=5? no so append [6,7] to merged
merged = [[1,5], [6,7]]

-------------------------------------------------------------------------------------------------------------------

Input: intervals = [[1,2],[2,3]]

merged= [1,2]

[2,3]
start=2 end=3
2<=3? yes
merged[i][1]= max(2,3)
merged= [1,3]


"""
