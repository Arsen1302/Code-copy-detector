class Solution:
    def solution_20_3(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            l=len(q)
            lvl=[]
            for i in range(l):
                node=q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                ans.append(lvl)
        return ans[::-1]