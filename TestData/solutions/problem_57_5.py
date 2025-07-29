class Solution:
    def solution_57_5(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if root:
            res+= [root.val]
            res+= self.solution_57_5(root.left)
            res+= self.solution_57_5(root.right)
        return res