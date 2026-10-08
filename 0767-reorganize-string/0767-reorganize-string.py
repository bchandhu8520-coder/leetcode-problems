class Solution:
    def reorganizeString(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        max_char = max(count, key=count.get)

        if count[max_char] > (len(s) + 1) // 2:
            return ""

        result = [""] * len(s)

        index = 0

        while count[max_char] > 0:
            result[index] = max_char
            index += 2
            count[max_char] -= 1

        for ch in count:
            while count[ch] > 0:
                if index >= len(s):
                    index = 1

                result[index] = ch
                index += 2
                count[ch] -= 1

        return "".join(result)