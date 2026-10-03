class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]

        for i in range(len(s), -1, -1):
            if s[:i] == rev[len(s) - i:]:
                return rev[:len(s) - i] + s

        return ""