class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(text):
            return text == text[::-1]

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if is_palindrome(part):
                    current.append(part)

                    backtrack(end, current)

                    current.pop()

        backtrack(0, [])

        return result