class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            groups[sorted_word].append(word)

        return list(groups.values())

'''
tc: O(n * klogk)
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

approach 1: sorting

groups = {}

sort act--> (a,c,t) not in groups --> groups = {(a,c,t): [act]}
sort pots --> (o,p,s,t) not in groups --> groups = {(a,c,t): [act], (o,p,s,t): [pots]}
sort tops --> in grp so append groups = {(a,c,t): [act], (o,p,s,t): [pots, tops]}
and so on

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]



'''