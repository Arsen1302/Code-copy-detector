class Solution:
    def solution_702_1_1(self, root: Optional[TreeNode]) -> int:
        def solution_702_1_2(node, path):
            if not node: return 0

            path = (path << 1) + node.val
			
            if not node.left and not node.right:
                return path
            
            return solution_702_1_2(node.left, path) + solution_702_1_2(node.right, path)
            
        return solution_702_1_2(root, 0)