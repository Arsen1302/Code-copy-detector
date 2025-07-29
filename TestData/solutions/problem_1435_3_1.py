class Solution:
    def solution_1435_3_1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def solution_1435_3_2(root,p,q):
            if not root: return None
            if root.val==p or root.val==q:
                return root
            L=solution_1435_3_2(root.left,p,q)
            R=solution_1435_3_2(root.right,p,q)
            if L and R:
                return root
            return L or R
        
        
        def solution_1435_3_3(node1,node2,path): #---> Problem here
            if not node1: return
            if node1.val==node2: return path
            return solution_1435_3_3(node1.left,node2,path+["L"]) or solution_1435_3_3(node1.right,node2,path+["R"])
            
        
        LCA=solution_1435_3_2(root,startValue,destValue)
        path1=solution_1435_3_3(LCA,startValue,[]) 
        path2=solution_1435_3_3(LCA,destValue,[])
        path=["U"]*len(path1) + path2 if path1 else path2 
        return "".join(path)