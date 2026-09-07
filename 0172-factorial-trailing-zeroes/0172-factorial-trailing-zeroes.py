class Solution(object):
    def trailingZeroes(self, n):
        count = 0

        while n > 0:
            n = n // 5
            count = count + n

        return count
        