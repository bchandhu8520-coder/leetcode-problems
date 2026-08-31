class Solution:
    def copyRandomList(self, head):

        # Phase 1: If head is null
        if head is None:
            return None

        # Phase 2: Create map
        map = {}

        # Phase 3: Current = head
        current = head

        # Phase 4: While loop
        # Map current node to a new/copy node
        while current:
            map[current] = Node(current.val)
            current = current.next

        # Phase 5: Current = head again
        current = head

        # Phase 6: Use map function to get next and random
        while current:
            map[current].next = map.get(current.next)
            map[current].random = map.get(current.random)

            current = current.next

        # Phase 7: Return statement
        return map[head]