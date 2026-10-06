class Solution:
    def gardenNoAdj(self, n, paths):
        graph = [[] for _ in range(n)]

        for a, b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        answer = [0] * n

        for garden in range(n):
            used = set()

            for neighbor in graph[garden]:
                if answer[neighbor] != 0:
                    used.add(answer[neighbor])

            for flower in range(1, 5):
                if flower not in used:
                    answer[garden] = flower
                    break

        return answer