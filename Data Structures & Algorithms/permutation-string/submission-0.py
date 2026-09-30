from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = Counter(s1)
        freq2 = Counter(s2[:len(s1)])
        left=0 

        if freq1==freq2:
            return True

        for right in range(len(s1),len(s2)):
            freq2[s2[right]]+=1

            freq2[s2[left]]-=1

            if freq2[s2[left]]==0:
                del freq2[s2[left]]

            left+=1

            if freq1==freq2:
                return True

        return False


'''
tc: O(n)
sc: O(1)   at most 26 lowercase letters

goal - Return true if s2 contains a permutation of s1, or false otherwise.

Approach: Fixed-size Sliding Window

1. Find frequency of s1.
2. Create a window of size len(s1) in s2.
3. Compare the two frequency maps.
4. Slide the window:
       - add s2[right]
       - remove s2[left]
       - move left
5. If frequencies match at any point, return True. Otherwise return False.

l e c a b e e
        r
    l

freq1= {a:1 b:1 c:1}

freq2 = {c:1 a:1 b:1}


'''