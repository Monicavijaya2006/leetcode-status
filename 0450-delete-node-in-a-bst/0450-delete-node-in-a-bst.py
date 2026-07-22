class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        target = root
        
        
        while target:
            if target.val == key:
                break
            
            
            parent = target
            
            
            if target.val > key:
                target = target.left
            else:
                target = target.right
        
        
        if not target or target.val != key:
            return root
        
        
        new_child = None
        
        
        if target.left and target.right:
            successor_parent = target
            successor = target.right
            
            
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            
            if successor_parent == target:
                successor_parent.right = None
            else:
                successor_parent.left = successor.right
                successor.right = target.right
            
            
            successor.left = target.left
            new_child = successor
        else:
            new_child = target.left if target.left else target.right
        
        
        if not parent:
            return new_child
        elif parent.left == target:
            parent.left = new_child
        else:
            parent.right = new_child
        
        
        return root