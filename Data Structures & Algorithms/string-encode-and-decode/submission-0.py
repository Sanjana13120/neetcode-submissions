class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)

        # print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            idx = int(s.find("#", i))
            length = int(s[i:idx])
            word = s[idx + 1 : idx + 1 + length]
            res.append(word)

            i = idx + 1 + length

        return res


"""
tc: O(n+m)
sc: O(n+m)

n = number of strings in the list.
m = total number of characters across all strings.

goal - encode and decode the string

Encode: Convert the list into a single string.
Decode: Convert that single string back into the original list.

1. Encode
Input: strs = ["Hello","World"]

convert to HelloWorld

so we need the len 

so enocode the list to --> 5#Hello5#World

2. Decode

1. find the #.
2. extract the word 
3. move to next word


5 # H e l l o 5 # W o r l d
i
i=0
idx = 1
length=5
word= s[2:7] = Hello

res = []

i=7
idx=8
length=s[7:8]=5
word=s[9:14]=world

res =  ["Hello","World"]



"""
