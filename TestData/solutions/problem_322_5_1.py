class Solution:
    def solution_322_5_1(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.solution_322_5_2(root)
        return self.max_diameter
    
    def solution_322_5_2(self, root):
        if not root:
            return 0
        
        left_depth = self.solution_322_5_2(root.left)
        right_depth = self.solution_322_5_2(root.right)
        # get the diameter between two nodes
        diameter = left_depth + right_depth
        
        # get the maximum diameter
        self.max_diameter = max(self.max_diameter, diameter)
        return max(left_depth, right_depth) + 1