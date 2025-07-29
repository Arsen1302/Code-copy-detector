class Solution:
    def solution_639_2(self, root: Optional[TreeNode]) -> bool:
        
        res=[]
        from collections import deque
        q=deque()
        q.append((root,1))
        
        while q:
            node,ind=q.popleft()
            res.append(ind)
            if node.left:
                q.append((node.left,2*ind))
            if node.right:
                q.append((node.right,2*ind+1))
        
        for i in range(len(res)-1):
            if res[i+1]-res[i]!=1:
                return False
        
        return True