class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        freq = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] == w2[j]:
                    continue
                if w1[j] != w2[j]:
                    if freq[w1[j]] > freq[w2[j]]:
                        return False
                    break

        return True


"""
tc: O(N)
sc: O(1)

N = total number of characters across all words.

given words and order

goal - return True if the words are in sorted lexicographically order

1. build hashamp structure for order
2. compare adj words char by char and check if order[word1[i]]<order[word2[i]]

Input: words = ["dag","disk","dog"], order = "hlabcdefgijkmnopqrstuvwxyz"

{'h': 0, 'l': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'i': 9, 'j': 10, 'k': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

w1= dag w2=disk
d==d skip
a==i? no so ordr[a]<order[i]==2<9 yes valid

w1 = disk w3=dog
d==d yes
i==o? no so 9<14 yes
valid

return True
-----------------------------------------------------------------------------------------------------------------------------
Input: words = ["neetcode","neet"], order = "worldabcefghijkmnpqstuvxyz"

{'w': 0, 'o': 1, 'r': 2, 'l': 3, 'd': 4, 'a': 5, 'b': 6, 'c': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'm': 15, 'n': 16, 'p': 17, 'q': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'x': 23, 'y': 24, 'z': 25}

w1=neetcode w2=neet

n==n? yes skip
e==e? skip
e==e? skip
t==t? skip

len(word1)>len(word2):
invalid --False




"""
