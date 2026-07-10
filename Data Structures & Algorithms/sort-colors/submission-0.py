class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # Don't increment i here because the swapped element
                # from the right hasn't been processed yet.
            else:  # nums[i] == 1
                i += 1
        