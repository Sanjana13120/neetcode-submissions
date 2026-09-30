from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        freq_t = Counter(t)
        minlen = float("inf")
        currlen = 0
        formed = 0
        ans = [-1, -1]
        freq_s = defaultdict(int)

        if len(s) < len(t):
            return ""

        for right in range(len(s)):
            freq_s[s[right]] += 1

            if s[right] in freq_t and freq_s[s[right]] == freq_t[s[right]]:
                formed += 1

            while formed == len(freq_t):
                currlen = right - left + 1

                if currlen < minlen:
                    minlen = currlen
                    ans = [left, right]

                freq_s[s[left]] -= 1

                if freq_s[s[left]] == 0:
                    del freq_s[s[left]]

                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    formed -= 1

                left += 1

        start, end = ans

        return s[start : end + 1] if minlen != float("inf") else ""


"""
tc: O(n+m)
sc: O(1)

n = len(s)
m = len(t)
Only 52 possible characters → space is O(1).

Goal:
    Return the shortest substring of s containing all characters of t, including duplicates.

Approach:
    Variable-size sliding window.

    right → expand the window
    left  → shrink the window when valid

    formed: Number of different characters whose required frequency has been satisfied.

    formed == len(freq_t)
        → current window is valid
        → try shrinking from left

Input: s = "OUZODYXAZV", t = "XYZ"

o u z o d y x a z v
                  r   
            l

freqt ={x:1 y:1 z:1}
minlen=inf

freqs= {x:1 a:1 z:1 v:1}

right=9
left=6
formed = 2

formed==len(freq1)?yes
    currlen = 4<5?
    minlen = 4
    ans = [5,8]

left=5
right=8

return s[5:8] = yxaz


"""
