class Solution:
    def solution_416_3(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root if not root or root.val == val else self.solution_416_3(root.left if root.val > val else root.right, val)