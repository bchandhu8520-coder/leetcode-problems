class Solution:
    def diameterOfBinaryTree(self, root):
        self.answer = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.answer = max(self.answer, left + right)

            return max(left, right) + 1

        height(root)

        return self.answer