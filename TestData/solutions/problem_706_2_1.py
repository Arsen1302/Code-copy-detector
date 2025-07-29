class Solution:
    def solution_706_2_1(self, root: TreeNode) -> int:
        self.maxx = 0
        self.solution_706_2_2(root)
        return self.maxx
    
    def solution_706_2_2(self, root):
        if not root.left and not root.right: return root.val, root.val
        
        if not root.left: l_min, l_max = root.val, root.val 
        else: l_min, l_max = self.solution_706_2_2(root.left)
            
        if not root.right: r_min, r_max = root.val, root.val
        else: r_min, r_max = self.solution_706_2_2(root.right)
        
        self.maxx=max(self.maxx,abs(root.val-l_min),abs(root.val-l_max),abs(root.val-r_min),abs(root.val-r_max))
        return min(root.val,l_min,r_min), max(root.val,l_max,r_max)