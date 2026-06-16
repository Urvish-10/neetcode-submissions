class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_seen = set()

        for right in range(len(s)):
            while s[right] in last_seen:
                last_seen.remove(s[left])
                left += 1
            last_seen.add(s[right])
            max_length = max(max_length, len(last_seen))
        return max_length
