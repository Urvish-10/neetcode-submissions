class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2  # avoids overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1  # discard left half
            else:
                high = mid - 1  # discard right half

        return low