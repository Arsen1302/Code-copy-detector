class Solution:
    def solution_1673_3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q,c = [root],0
        while q:
            c+=1
            n = len(q)
            if c%2==0:
                s,e = 0,n-1
                while s<e:
                    q[s].val,q[e].val = q[e].val,q[s].val
                    s+=1
                    e-=1
            for i in range(n):
                x = q.pop(0)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        
        return root