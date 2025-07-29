class Solution:
    def solution_18_2_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        loc = {x: i for i, x in enumerate(inorder)}
        pre = iter(preorder)
        
        def solution_18_2_2(lo, hi): 
            """Return node constructed from inorder[lo:hi]."""
            if lo == hi: return None
            k = loc[next(pre)]
            return TreeNode(inorder[k], solution_18_2_2(lo, k), solution_18_2_2(k+1, hi))
        
        return solution_18_2_2(0, len(inorder))