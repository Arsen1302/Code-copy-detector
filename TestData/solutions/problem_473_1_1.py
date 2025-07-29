class Solution:
    def solution_473_1_1(self, root: Optional[TreeNode]) -> int:
        
        # list with two element
        # the first for the previous element
        # the second for the min value
        pre_mn = [-float("inf"), float("inf")]
        
        def solution_473_1_2(tree):
            
            if not tree:
                return
            
            # Keep going to the left
            solution_473_1_2(tree.left)
            
            # if we can't go further, update min and pre
            pre_mn[1] = min(pre_mn[1], abs(tree.val) - pre_mn[0])
            pre_mn[0] = tree.val
            
            # keep traversing in-order
            solution_473_1_2(tree.right)
        
        solution_473_1_2(root)
        
        # return min (the second element in the list)
        return pre_mn[1]