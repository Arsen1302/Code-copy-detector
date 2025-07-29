class Solution:
    def solution_361_4_1(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, root)
        
        def solution_361_4_2(node, depth):
            if node:
                if depth == 1:
                    node.left  = TreeNode(val, left  = node.left)
                    node.right = TreeNode(val, right = node.right)

                solution_361_4_2(node.left, depth - 1)
                solution_361_4_2(node.right, depth - 1)
            
        solution_361_4_2(root, depth - 1)
        
        return root