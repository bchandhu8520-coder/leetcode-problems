class Solution:
    def recoverTree(self, root):
        stack = []
        current = root
        previous = None
        first = None
        second = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous and previous.val > current.val:
                if first is None:
                    first = previous
                second = current

            previous = current
            current = current.right

        first.val, second.val = second.val, first.val