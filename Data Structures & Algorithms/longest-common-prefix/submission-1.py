class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_tuples = takewhile(
        lambda x: len(set(x)) == 1,  # all same letters
        zip(*strs)
        )
        # Join the first element of each tuple (since they're identical)
        return ''.join(chars[0] for chars in prefix_tuples)