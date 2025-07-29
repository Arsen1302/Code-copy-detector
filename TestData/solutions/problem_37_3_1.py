class Solution:
    def solution_37_3_1(self, root: TreeNode) -> int:
        def solution_37_3_2(node):
            if not node:
                return (float('-inf'),float('-inf'))
            l_TBC,l_Complete = solution_37_3_2(node.left)
            r_TBC,r_Complete = solution_37_3_2(node.right)
            rt_TBC = max(node.val,node.val+l_TBC,node.val+r_TBC)
            rt_Complete = max(rt_TBC,node.val+l_TBC+r_TBC,l_Complete,r_Complete)
            return (rt_TBC,rt_Complete)
        return solution_37_3_2(root)[1]