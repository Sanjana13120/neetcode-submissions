from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        start = 0
        end = len(arr) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid][0] <= timestamp:
                start = mid + 1
                ans = arr[mid][1]
            else:
                end = mid - 1

        return ans if ans != -1 else ""


"""
tc: 
set(): O(1) per operation.

get(): O(logn) time using binary search.

Space:O(N), where N is the total number of stored entries.

goal - Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

approach: binary search

1. Use a dict to store { key: [(timestamp,value)] }
2. store in sorted order
3. set(): Store the timestamp and value under the given key.
4. get(): Use binary search on that key's list.
5. Maintain ans to remember the best valid candidate.
6. If no valid candidate is found, return "".

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]


"set", ["alice", "happy", 1]  --> map = {alice: [(1, happy)]}
"get", ["alice", 1] --> happy
"get", ["alice", 2] --> happy
"set", ["alice", "sad", 3] --> map = {alice: [(1, happy),(3,sad)]}
"get", ["alice", 3]] --> sad



"""
