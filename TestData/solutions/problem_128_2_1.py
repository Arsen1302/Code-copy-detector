class Solution:
    def solution_128_2_1(self, root: Optional[TreeNode], cur, res) -> None:
        
        # Base Case
        if not root:
            return
        
        # Append node to path
        cur.append(str(root.val))
        
        # If root is a leaf, append path to result
        if not root.left and not root.right:
            res.append('->'.join(cur))
            
        # Recursive Step
        self.solution_128_2_1(root.left, cur, res)
        self.solution_128_2_1(root.right, cur, res)
        
        # Backtracking / Post-processing / pop node from path
        cur.pop()
        
        
    def solution_128_2_2(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.solution_128_2_1(root, [], res)
        return res