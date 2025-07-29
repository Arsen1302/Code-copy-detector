class Solution:
    def solution_912_2_1(self, root: TreeNode) -> int:
        
        def solution_912_2_2(node): 
            """Collect info while traversing the tree in post-order."""
            if not node: return True, inf, -inf, 0, 0 # bst flag | min | max | sum
            ltf, lmn, lmx, lsm, lval = solution_912_2_2(node.left)
            rtf, rmn, rmx, rsm, rval = solution_912_2_2(node.right)
            lmn = min(lmn, node.val)
            rmx = max(rmx, node.val)
            sm = lsm + rsm + node.val 
            if ltf and rtf and lmx < node.val < rmn: 
                return True, lmn, rmx, sm, max(lval, rval, sm)
            return False, lmn, rmx, sm, max(lval, rval)
        
        return solution_912_2_2(root)[-1]