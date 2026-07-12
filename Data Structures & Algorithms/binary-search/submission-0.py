class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:                          
            mid = lo + (hi - lo) // 2           # avoids overflow

            if nums[mid] == target:
                return mid                      
            elif nums[mid] < target:
                lo = mid + 1                     # discard left half
            else:
                hi = mid - 1                     # discard right half

        return -1 