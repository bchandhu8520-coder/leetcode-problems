class Solution:
    def stringMatching(self, words):
        answer = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    answer.append(words[i])
                    break

        return answer