class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            max_freq = max(max_freq, char_count[char])
            
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans