from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxlen = 0
        maxfreq = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1
            maxfreq = max(maxfreq, freq[s[right]])

            while (right - left + 1) - maxfreq > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen


"""
tc: O(n)
sc: O(n)

Goal:
    Find the length of the longest substring that can be changed into a substring of the same character using at most k replacements.

Approach: Sliding Window + Frequency Map

Key idea:
    For the current window, keep the character that appears most often.
    replacements needed =  window length - maxfreq

    If replacements needed <= k:
        the window is valid.

    If replacements needed > k:
        the window is invalid, so move left forward to shrink it.

Input: s = "XYYX", k = 2

X Y Y X  k=2
      r
l

freq = {x:2 y:2}
right = 3
left=0

maxfreq= 2

maxlen=4


---------------------------------------------------------

Input: s = "AAABABB", k = 1

A A A B A B B
            r 
    l

freq = {A:2 B:3}
right=6
left=2

maxfreq=4
maxlen=5

"""
