class Solution:
    def solution_88_3_1(self, root: TreeNode) -> List[int]:
        res, max_level = [], -1
        
        def solution_88_3_2(node, level):
            nonlocal res, max_level
            if not node:
                return
            if max_level < level:
                res.append(node.val)
                max_level = level
            solution_88_3_2(node.right, level + 1)
            solution_88_3_2(node.left, level + 1)
        
        solution_88_3_2(root, 0)
        return res