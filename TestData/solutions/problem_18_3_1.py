class Solution:
    def solution_18_3_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        loc = {x: i for i, x in enumerate(inorder)}
        k = 0 
        
        def solution_18_3_2(lo, hi): 
            """Return BST constructed from inorder[lo:hi]."""
            nonlocal k 
            if lo < hi: 
                val = preorder[k]
                mid = loc[val]
                k += 1
                return TreeNode(val, solution_18_3_2(lo, mid), solution_18_3_2(mid+1, hi))
        
        return solution_18_3_2(0, len(inorder))