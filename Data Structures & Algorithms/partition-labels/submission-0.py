class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = {}

        for i, ch in enumerate(s):
            lastidx[ch] = i

        start = end = 0
        res = []

        for i,ch in enumerate(s):
            end=max(end,lastidx[ch])

            if i==end:
                res.append((end-start+1))
                start = i+1

        return res


"""
tc: O(n)
sc: O(n)  since 26 chars --> O(1)
goal - Return a list of integers representing the size of these substrings in the order they appear in the string.

Approach: greedy

1. Traverse the string once to store the last occurrence (index) of each character in a dictionary.

2. Initialize start and end to 0, and create an empty result list.
   - start represents the beginning of the current partition.
   - end represents the farthest index the current partition must reach.

3. Traverse the string again:
   - Update end = max(end, lastidx[ch]) to ensure the current partition includes the last occurrence of every character encountered.
   - When i == end, all characters in the current partition have their last occurrences within the partition. Therefore, we can safely finalize the partition.
   - Append the partition size (end - start + 1) to the result list and set start = i + 1 to begin the next partition.

4. Return the result list.

Input: s = "xyxxyzbzbbisl"

0 1 2 3 4 5 6 7 8 9 10 11 12
x y x x y z b z b b  i  s  l

lastidx = {x:3 y:4 z:7 b:9 i:10 s:11 l:12}

end=0
start=0
res= []

i=0    end=max(0,3)=3   0==3? no
i=1    end=max(3,4)=4   1==4?no
i=2    end=4     2==4?no
i=3    end=4    3==4?no
i=4    end=4    4==4? yes res[0]=4-0+1=5 res=[5]
       start=5

i=5    end=max(4,7)=7 5==7?no
i=6    end=9    6==9?no
i=7    end=9    7==9?no
i=8    end=9    8==9?no
i=9    end=9    9==9? yes end-start+1 = 9-5+1=5 res=[5,5] start=10
i=10   end=10   10==10? yes 10-10+1=1 res=[5,5,1] start=11
i=11   end=11   11==11? yes 11-11+1=1 res=[5,5,1,1]  start=12
i=12   end=12   12==12? yes 12-12+1=1  res=[5,5,1,1,1]   start=13


return res=[5,5,1,1,1]


-------------------------------------------------------------------------------------------------------------------

Input: s = "abcabc"

0 1 2 3 4 5
a b c a b c

lastindex  = {a:3 b:4 c:5}

start=end=0
res= []

i=0     end= 3      0==3? no
i=1     end= 4      1==3?no
i=2     end= 5      2==5? no
i=3     end= 5      3==5? no
i=4     end= 5      4==5? no
i=5     end=5       5==5? yes 5-0+1=6  res=[6] start=6


"""
