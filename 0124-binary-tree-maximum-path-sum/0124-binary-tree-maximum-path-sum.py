class Solution:
    def maxPathSum(self, root):
        self.answer = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            current = node.val + left + right

            self.answer = max(self.answer, current)

            return node.val + max(left, right)

        dfs(root)

        return self.answer