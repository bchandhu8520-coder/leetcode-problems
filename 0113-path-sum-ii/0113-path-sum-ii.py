class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, total):
            if node is None:
                return

            path.append(node.val)
            total += node.val

            if node.left is None and node.right is None:
                if total == targetSum:
                    result.append(path[:])

            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)

        return result