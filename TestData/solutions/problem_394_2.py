class Solution:
    def solution_394_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        r, l = [root], []
        
        while r:
            n = r.pop(0)
            l.append(n.val)
            if n.right: r.append(n.right)
            if n.left:  r.append(n.left)
                
        l = sorted(list(set(l)))
        
        if len(l) == 1:
            return -1
        return l[1]