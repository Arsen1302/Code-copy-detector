class Solution:
    
    def solution_27_2_1(self):
        self.prev = None
    
    def solution_27_2_2(self, root):
        if not root:
            return None
        self.solution_27_2_2(root.right)
        self.solution_27_2_2(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root