class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        res = []
        i = j = 0

        while i < len1 or j < len2:
            if i < len1:
                res.append(word1[i])
                i += 1

            if j < len2:
                res.append(word2[j])
                j += 1

        return "".join(res)


"""
tc: O(n+m)
sc: O(n+m)


Approach: Two Pointers

1. Initialize two pointers:
   i = 0 for word1
   j = 0 for word2
2. Create an empty list to store the merged characters.
3. Use a while loop:
   Continue while i < len1 OR j < len2.
4. If i < len1:
   Append word1[i] to result.
   Increment i.
5. If j < len2:
   Append word2[j] to result.
   Increment j.
6. Join the result list into a string and return it.

Input: word1 = "abc", word2 = "xyz"

len1=3 
len2=3

i=0 j=0
    0<3 i=1
    0<3 j=1
i=1 j=1



res= [axbycxz]
axbycxz


"""
