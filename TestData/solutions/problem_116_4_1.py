class Solution:
    def solution_116_4_1(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = 0
        
        def solution_116_4_2(node: Optional[TreeNode]) -> None:
            nonlocal count, ans
            if not node:
                return
            
            solution_116_4_2(node.left)
            
            count += 1
            if count == k:
                ans = node.val
                return
            
            solution_116_4_2(node.right)
        
        solution_116_4_2(root)
        return ans