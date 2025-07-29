class Solution:
    def solution_215_3_1(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def solution_215_3_2(node,ans,check):
            if not node:
                return
            if not node.left and not node.right and check:
                # print(node.val)
                ans[0]+=node.val
                return
            solution_215_3_2(node.left,ans,True)
            solution_215_3_2(node.right,ans,False)
            return
        solution_215_3_2(root,ans,False)
        return ans[0]