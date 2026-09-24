class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        n = len(nums)

        small = (n + 1) // 2 - 1
        large = n - 1

        result = [0] * n

        for i in range(0, n, 2):
            result[i] = nums[small]
            small -= 1

        for i in range(1, n, 2):
            result[i] = nums[large]
            large -= 1

        nums[:] = result