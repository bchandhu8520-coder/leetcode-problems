class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_defense = 0
        answer = 0

        for attack, defense in properties:
            if defense < max_defense:
                answer += 1

            max_defense = max(max_defense, defense)

        return answer