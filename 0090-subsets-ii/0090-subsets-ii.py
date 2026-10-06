class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        result = [[]]

        for i in range(len(nums)):
            start = 0

            if i > 0 and nums[i] == nums[i - 1]:
                start = previous_size

            previous_size = len(result)

            for j in range(start, previous_size):
                result.append(result[j] + [nums[i]])

        return result