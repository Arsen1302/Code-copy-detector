class Solution:
    def solution_668_3_1(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def solution_668_3_2(root,ds):
            ds.append(chr(97+root.val))
            if not root.left and not root.right:
                ans.append("".join(ds[:]))
                return
            if root.left:
                solution_668_3_2(root.left,ds)
                ds.pop()
            if root.right:
                solution_668_3_2(root.right,ds)
                ds.pop() 
        solution_668_3_2(root,[])
        ans=sorted([i[::-1] for i in ans])
        return ans[0]