class Solution:
def solution_886_4_1(self, root: Optional[TreeNode]) -> int:
    
    def solution_886_4_2(root):
        if root is None:
            return 0
        ans = solution_886_4_2(root.left)+solution_886_4_2(root.right)+root.val
        res.append(ans)
        return ans
    
    res=[]
    solution_886_4_2(root)
    
    total,m = max(res),float('-inf')
    for s in res:
        m=max(m,s*(total-s))
        
    return m%(10**9+7)