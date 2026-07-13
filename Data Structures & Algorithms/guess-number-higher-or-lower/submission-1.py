# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, i = 0, j = None) -> int:
        if j is None:
            j = n

        g = (i+j) // 2
        res = guess(g)
        if res == -1:
            return self.guessNumber(n, i, g)
        elif res == 1:
            return self.guessNumber(n, g+1, j)
        else:
            return g