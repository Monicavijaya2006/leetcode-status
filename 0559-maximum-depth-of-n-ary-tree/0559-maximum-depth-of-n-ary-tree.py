from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None,
                 children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        op = 0

        q = deque([root])

        while q:
            op += 1

            for _ in range(len(q)):
                node = q.popleft()

                q += node.children

        return op