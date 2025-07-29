class Solution:
    def solution_27_1_1(self):
        self.prev = None
        
    def solution_27_1_2(self, root: Optional[TreeNode]) -> None:
        
        if not root: return 
        self.solution_27_1_2(root.right)
        self.solution_27_1_2(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root