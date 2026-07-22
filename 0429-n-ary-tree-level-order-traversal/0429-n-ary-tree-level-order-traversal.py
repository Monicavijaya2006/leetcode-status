from collections import deque
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None,
                 children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        op = []

        q = deque([root])

        while q:
            lvl = []

            for _ in range(len(q)):
                node = q.popleft()

                lvl.append(node.val)

                q += node.children

            op.append(lvl)

        return op