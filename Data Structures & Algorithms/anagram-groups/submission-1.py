class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)

        for word in strs:
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord('a')] +=1

            groups[tuple(count)].append(word)

        return list(groups.values())

        

'''

tc: O(n*k)
sc: O(n*k)

n = number of strings
k = maximum length of a string

Input: strs = ["act","pots","tops","cat","stop","hat"]

1. count the frequency.
2. if same freq, group it and append to res

act, cat - {a:1 c:1 t:1}
pots, tops, stop - {p:1 o:1 t:1 s:1}
hat - {h:1 a:1 t:1}

res = [[act,cat], [pots,tops,stop], [hat]]

approach 2: 

groups = {}

act - (a:1 b:0 c:1 ..... t:1 ... z:0)
cat - (a:1 b:0 c:1 ..... t:1 ... z:0)
then append to groups
'''