class Solution:
    def flatten(self, head):
        if head is None:
            return None

        current = head

        while current:
            if current.child:
                next_node = current.next

                child = self.flatten(current.child)

                current.next = child
                child.prev = current
                current.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                tail.next = next_node

                if next_node:
                    next_node.prev = tail

            current = current.next

        return head