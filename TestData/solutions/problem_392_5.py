class Solution:
    def solution_392_5(self, root: TreeNode, low: int, high: int) -> TreeNode:
		# base case
        if not root:
            return
        
		# trim left and right subtree
        root.left = self.solution_392_5(root.left, low, high)
        root.right = self.solution_392_5(root.right, low, high)        
    
		# if node's value is out of bounds
		# we appropriately replace the current node
        if root.val < low:
            root = root.right
        elif root.val > high:
            root = root.left
            
        return root