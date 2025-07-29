class Solution:
    def solution_416_1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val==val:
            return root
        if root.val<val:
            return self.solution_416_1(root.right,val)
        else:
            return self.solution_416_1(root.left,val)