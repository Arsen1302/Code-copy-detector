class Solution:
    def solution_298_1(self, root: Optional[TreeNode]) -> int:
        q=[[root]]
        nodes=[]
        while q:
            nodes = q.pop(0)
            t=[]
            for n in nodes:
                if n.left:
                    t.append(n.left)
                if n.right:
                    t.append(n.right)
            if t:
                q.append(t)
        return nodes[0].val
# Please upvote if you understand the solution