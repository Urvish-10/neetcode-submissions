class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for key, val in enumerate(nums):
            if val in seen:
                return True
            seen[val] = key
        return False