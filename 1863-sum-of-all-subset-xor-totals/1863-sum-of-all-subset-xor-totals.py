class Solution:
    def subsetXORSum(self, nums):
        def solve(index, xor_value):
            if index == len(nums):
                return xor_value

            not_take = solve(index + 1, xor_value)
            take = solve(index + 1, xor_value ^ nums[index])

            return not_take + take

        return solve(0, 0)