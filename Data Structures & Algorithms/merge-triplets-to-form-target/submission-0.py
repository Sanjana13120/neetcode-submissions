class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False]*3

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, x in enumerate(t):
                if x == target[i]:
                    good[i]=True

        return all(good)


"""
tc: O(n)
sc: O(1)
goal - Return true if it is possible to obtain target as an element of triplets, or false otherwise.

Approach: Greedy

1. Initialize a boolean list good = [False, False, False] to track whether each target position can be achieved.
2. Iterate through all triplets.
3. Filter unsafe triplets: If any element of a triplet is greater than its corresponding target element, skip it.
    Reason: We use the max() operation, so values can only increase, never decrease.
4. For every safe triplet:
    Compare each element with its corresponding target element.
    If t[i] == target[i], mark good[i] = True.
5. After processing all triplets:
    Return all(good).
    If all three positions are matched, return True; otherwise, return False.

Key intuition: We don't need to actually merge triplets. We only need to find safe triplets that collectively contribute all three target values. The matching values can come from different triplets.


Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]

max(1,7)=7 max(2,1)=2 max(3,1)=3
[7,2,3] == target: so true

good = [F F F]

[1,2,3]
1==7? no
2==2? yes good = [F T F]
3==3? yes good = [F T T]

[7,1,1]
7==7? yes good = [T T T]
1==2? no
1==3? no

so all(good) yes? return true

-------------------------------------------------------------------------------------
Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]

choose 1st 2nd 
max(2,1)=2 max(5,4)=5 max(6,4)=6
[2,5,6]==[5,4,6] --> no
then choose merged [2,5,6] and [5,7,5]
[5,7,5]==[5,4,6] --> no


max(1,5)=5 max(4,7)=7 max(6,5)=6
[5,7,6]==[5,4,6] --> no
then choose merged [5,7,6] and [2,5,6]
[5,7,6]==[5,4,6]--> no

false

[2,5,6]
2>5 or 5>4 or 6>6? yes so skip

[1,4,4] 
1==5? no
4==4? yes good = [F T F]
4==6? no

[5,7,5]
5>5 or 7>4 or 5>6? yes so skip

all(good)? no
return False


"""
