class Solution:
    def solution_359_4_1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return Solution.solution_359_4_2(self, root1, root2) 
        
    def solution_359_4_2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        ans = TreeNode(Solution.solution_359_4_3(self, root1, root2))
        
        if root1 and root2:
            ans.left = Solution.solution_359_4_2(self, root1.left, root2.left)
            ans.right = Solution.solution_359_4_2(self, root1.right, root2.right)

        return ans
    
    def solution_359_4_3(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[int]:
        if p and q:
            return p.val + q.val
        elif p:
            return p.val
        elif q:
            return q.val
        else:
            return None