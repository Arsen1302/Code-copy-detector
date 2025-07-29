class Solution:
    def solution_619_1(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        res = 0
        
        q = deque([root])
        while q:
            c = q.popleft()
            v, l, r = c.val, c.left, c.right

            if lo <= v and v <= hi:
                res += v
                
            if l and (lo < v or v > hi):
                q.append(l)
                
            if r and (lo > v or v < hi):
                q.append(r)
            
        return res