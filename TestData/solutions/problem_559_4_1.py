class Solution:
    def solution_559_4_1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solution_559_4_2(rt):
            if not rt:
                return []
            elif not rt.left and not rt.right:
                return [rt.val]
            else:
                lv = solution_559_4_2(rt.left)
                rv= solution_559_4_2(rt.right)
                return lv+rv 
        lst1 = solution_559_4_2(root1)
        lst2 = solution_559_4_2(root2)
        return True if lst1 ==lst2 else False