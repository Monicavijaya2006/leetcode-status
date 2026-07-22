class Solution:
    def reverseKGroup(self, head, k):
        node = head

        # Check if there are at least k nodes
        for i in range(k):
            if not node:
                return head
            node = node.next

        # Reverse first k nodes
        prev = None
        curr = head

        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev