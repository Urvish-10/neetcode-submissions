class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map=set(nums)
        if len(map)!=len(nums):
            return True
        return False