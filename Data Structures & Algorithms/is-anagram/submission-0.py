class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)



'''
tc: O(n)
sc: O(1)

'''