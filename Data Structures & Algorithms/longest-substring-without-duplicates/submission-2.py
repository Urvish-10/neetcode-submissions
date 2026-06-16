class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        max_length = 0
        last_seen = [-1] * (256)
        for right in range(len(s)):
            if last_seen[ord(s[right])] > left:
                left = last_seen[ord(s[right])]

            max_length = max(max_length, right - left)
            last_seen[ord(s[right])] = right

        return max_length
