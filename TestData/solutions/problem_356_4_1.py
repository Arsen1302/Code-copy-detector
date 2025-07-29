class Solution:
    def solution_356_4_1(self, root: Optional[TreeNode]) -> str:
        ans=""
        def solution_356_4_2(root):
            nonlocal ans
            if root is None:
                return
            ans+=str(root.val)+"("
            solution_356_4_2(root.left)
            ans+=")("
            solution_356_4_2(root.right)
            if ans[-1]=="(":
                ans=ans[:-1]
            else:
                ans+=')'
            if ans[-2:]=='()':
                ans=ans[:-2]
            
        solution_356_4_2(root)
        return ans