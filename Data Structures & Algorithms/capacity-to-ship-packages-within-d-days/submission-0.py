class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right - left) // 2

            required_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    required_days += 1
                    current_weight = weight

            if required_days <= days:
                right = mid - 1   # Try smaller capacity
            else:
                left = mid + 1    # Need bigger capacity

        return left
        