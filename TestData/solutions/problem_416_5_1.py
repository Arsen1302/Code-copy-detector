class Solution:
    def solution_416_5_1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def solution_416_5_2(root):
            if root == None:
                return None
            if root.val == val:
                return root
            if val < root.val:
                return solution_416_5_2(root.left)
            else:
                return solution_416_5_2(root.right)
        
        return solution_416_5_2(root)