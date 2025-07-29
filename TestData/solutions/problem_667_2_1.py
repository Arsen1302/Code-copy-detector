class Solution:
    def solution_667_2_1(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def solution_667_2_2(root,r,c):
            if root:
                ans.append([r,c,root.val])
                solution_667_2_2(root.left,r+1,c-1)
                solution_667_2_2(root.right,r+1,c+1)
            return
        solution_667_2_2(root,0,0)
        ans=sorted(ans,key=lambda x:(x[1],x[0],x[2]))
        d=defaultdict(list)
        for i,j,k in ans:
            d[j].append(k)
        l=[]
        for i in d.values():
            l.append(i)
        return l