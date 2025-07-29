class Solution:
    def solution_57_2_1(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        def solution_57_2_2(node):
            if node:
                ans.append(node.val)
                solution_57_2_2(node.left)
                solution_57_2_2(node.right)
            
        solution_57_2_2(root)
        return ans