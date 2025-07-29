class Solution:
    def solution_416_2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val: # If end is reached or a node with a value of target is found found.
            return root # Return that node.
		# If target > current nodes value search in left side of node else search rightwards.
        return self.solution_416_2(root.left,val) if root.val > val else self.solution_416_2(root.right,val)