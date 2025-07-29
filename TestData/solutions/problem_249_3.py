class Solution:
    def solution_249_3(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root: 
            if root.val < key: root.right = self.solution_249_3(root.right, key)
            elif root.val == key: 
                if not root.left or not root.right: return root.left or root.right 
                node = root.right 
                while node.left: node = node.left 
                root.val = node.val 
                root.right = self.solution_249_3(root.right, node.val)
            else: root.left = self.solution_249_3(root.left, key)
        return root