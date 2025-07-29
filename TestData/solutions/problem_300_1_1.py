class Solution:
    def solution_300_1_1(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def solution_300_1_2(root, depth):
            if root is None:
                return
            
            if depth == len(res):
                res.append(root.val)
            else:
                res[depth] = max(res[depth], root.val)
            
            solution_300_1_2(root.left, depth + 1)
            solution_300_1_2(root.right, depth + 1)
        
        solution_300_1_2(root, 0)
        return res