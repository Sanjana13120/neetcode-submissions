class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            maxlen = max(maxlen, right - left + 1)

        return maxlen


"""
tc: O(n)
sc: O(n)

goal - find the length of the longest substring without duplicate characters. 

Approach: Sliding Window + Set
    left and right represent the current window.
    seen stores the characters currently inside the window.
    If s[right] is already in seen:
        Remove characters from the left until s[right] is no longer duplicated.
    Then add s[right] to seen and update the maximum length.


z x y z x y z
            r
        l

right = 6
left = 4
seen = (x y z)
count = 3

"""
