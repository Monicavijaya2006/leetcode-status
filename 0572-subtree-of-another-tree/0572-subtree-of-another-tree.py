# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  

    def isSame(self, node, subRoot):
        if (node and not subRoot) or (not node and subRoot):
            return False
        if not node and not subRoot:
            return True
        if node.val != subRoot.val:
            return False
        l = self.isSame(node.left, subRoot.left)
        r = self.isSame(node.right, subRoot.right)
        return l and r