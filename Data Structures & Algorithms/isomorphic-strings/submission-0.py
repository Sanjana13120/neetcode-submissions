class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for i, j in zip(s, t):
            if i in smap and smap[i] != j:
                return False

            if j in tmap and tmap[j] != i:
                return False

            smap[i] = j
            tmap[j] = i

        return True


"""
tc: O(n)
sc: O(1)  (At most 256 ASCII characters, assuming ASCII input)

goal - determine if they are isomorphic - if the characters in s can be replaced to get t.

Approach:
1. Create two hashmaps:
   - smap: stores mapping from s -> t
   - tmap: stores mapping from t -> s
2. Iterate through both strings simultaneously using zip().
3. Check two conditions:
   a) If character i from s is already present in smap,
      check whether it maps to the current character j.
      If smap[i] != j:
          return False
   b) If character j from t is already present in tmap,
      check whether it maps to the current character i.
      If tmap[j] != i:
          return False
4. If both conditions pass:
      Store the mappings in both hashmaps.
5. If the loop completes:
      return True


Input: s = "egg", t = "add"

smap = {}
tmap = {}

0 1 2
e g g
    i

0 1 2
a d d
    j

smap = {e:a, g:d}
tmap = {a:e, d:g} 

d!=d no

return True

----------------------------------------------------------------------------------------------------
Input: s = "foo", t = "bar"

f o o 
    i 

b a r
    j

smap = {f:b, o:a}
tmap = {b:f, a:o}

a!=r yes return False
"""
