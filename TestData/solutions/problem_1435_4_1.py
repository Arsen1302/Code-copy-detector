class Solution:
    def solution_1435_4_1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        #soltion 2 LCA
        def solution_1435_4_2(root,p,q):
            if not root: return None
            if root.val==p or root.val==q:
                return root
            L=solution_1435_4_2(root.left,p,q)
            R=solution_1435_4_2(root.right,p,q)
            if L and R:
                return root
            return L or R
    
            
        
        LCA=solution_1435_4_2(root,startValue,destValue)
        ps,pd="",""
        stack = [(LCA, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
                
        return "U"*len(ps) + pd