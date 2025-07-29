class Solution:
    def solution_290_1_1(self, root: Optional[TreeNode]) -> List[int]:
        
        def solution_290_1_2(root: TreeNode) -> None:
            
            if not root:
                return
            
            nonlocal maxcount, count, prevval, modes
            
            solution_290_1_2(root.left)
            
            if root.val == prevval:
                count += 1
            else:                
                count = 1
                
            if count > maxcount:
                maxcount = count
                modes = [root.val]
            elif count == maxcount:
                modes.append(root.val)
                
            prevval = root.val
            solution_290_1_2(root.right)
                
                
        modes = []
        maxcount = 0
        count = 0
        prevval = root.val
        solution_290_1_2(root)
        
        return modes