class Solution:
    def solution_1610_3(self, root: TreeNode) -> bool:
                                #
                                # Recursion:
                                #
                                #   Base Case: node.val = 0 or 1. Return T or F
                                #   
                                #   Recursive Case: node.val = 2 or 3. Node value  is determined
								#   upon the  values l = node.left.val, r = node.right.val, 
                                #   and  v = T if node.val = OR  else F if node.val = AND
                                #
                                #   From a Venn diagram or a truth table for l, r, v, one can
                                #   see the return from the recursive call is l&amp;r or l&amp;v or r&amp;v
                                #
        if root.val<2: return root.val
        l = self.solution_1610_3(root.left)
        r = self.solution_1610_3(root.right)
        v = root.val^1

        return l&amp;r or l&amp;v or r&amp;v