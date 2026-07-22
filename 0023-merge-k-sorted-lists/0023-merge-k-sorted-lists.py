class Solution:
    def mergeKLists(self, lists):
        arr = []

        # Store all values
        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next

        # Sort values
        arr.sort()

        # Create new linked list
        dummy = ListNode(0)
        current = dummy

        for num in arr:
            current.next = ListNode(num)
            current = current.next

        return dummy.next