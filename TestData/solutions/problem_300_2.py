class Solution:
    def solution_300_2(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        if root:
            q.append(root)
        Max=[]
        while len(q)>0:
            arr=[]
            length=len(q)
            for i in range(len(q)):
                current=q.pop(0)
                arr.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            Max.append(max(arr))
        return Max;