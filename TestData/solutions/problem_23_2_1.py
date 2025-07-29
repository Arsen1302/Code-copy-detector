class Solution:
    def solution_23_2_1(self, root: Optional[TreeNode]) -> bool:
        return (self.solution_23_2_2(root) >= 0)
    def solution_23_2_2(self, root: Optional[TreeNode]) -> bool:
        if root is None:  return 0
        leftheight, rightheight = self.solution_23_2_2(root.left), self.solution_23_2_2(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1