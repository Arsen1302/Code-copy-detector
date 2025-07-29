class Solution:
    def solution_121_4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        l = self.solution_121_4(root.left, p, q)
        r = self.solution_121_4(root.right, p, q)
        
        if l and r :
            return root
        else:
            return l or r