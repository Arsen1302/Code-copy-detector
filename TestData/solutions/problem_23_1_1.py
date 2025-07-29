class Solution(object):
    def solution_23_1_1(self, root):
        return (self.solution_23_1_2(root) >= 0)
    def solution_23_1_2(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.solution_23_1_2(root.left), self.solution_23_1_2(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1