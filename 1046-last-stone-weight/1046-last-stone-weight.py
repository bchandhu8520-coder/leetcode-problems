class Solution:
    def lastStoneWeight(self, stones):
        stones.sort()

        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()

            if x != y:
                stones.append(y - x)

            stones.sort()

        if stones:
            return stones[0]

        return 0