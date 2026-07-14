class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            print(mid * mid)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans