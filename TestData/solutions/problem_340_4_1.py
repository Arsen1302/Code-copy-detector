class Solution:
    def solution_340_4_1(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def solution_340_4_2(root, subroot):
            if not root and not subroot: return True
            elif not root or not subroot: return False
            
            if root.val == subroot.val:
                if solution_340_4_2(root.left, subroot.left) and solution_340_4_2(root.right, subroot.right):
                    return True

                
        def solution_340_4_3(root, subroot):
            if not root: return
            
            if root.val == subroot.val and solution_340_4_2(root, subroot): res[0] = True
                        
            if root.left: solution_340_4_3(root.left, subroot)
            if root.right: solution_340_4_3(root.right, subroot)
        
        res = [False]
        solution_340_4_3(root, subroot) 
        return res[0]