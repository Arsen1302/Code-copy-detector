class Solution:
    def solution_970_3_1(self, root: TreeNode) -> int:
        
        def solution_970_3_2(node, _max):
            if not node: return 0
            
            curr = 1 if _max <= node.val else 0
            left = solution_970_3_2(node.left, max(_max, node.val))
            right = solution_970_3_2(node.right, max(_max, node.val))
            
            return curr+left+right

        return solution_970_3_2(root, root.val)