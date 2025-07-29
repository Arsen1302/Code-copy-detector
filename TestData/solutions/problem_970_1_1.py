class Solution:
    def solution_970_1_1(self, root: TreeNode) -> int:
        def solution_970_1_2(root,val):
            if root:
                k = solution_970_1_2(root.left, max(val,root.val)) + solution_970_1_2(root.right, max(val,root.val))
                if root.val >= val:
                    k+=1
                return k
            return 0
        return solution_970_1_2(root,root.val)