class Solution:
    def solution_861_4(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        m=len(queries)
        prefixXor=[0 for i in range(n)]
        ans=[]
        for i in range(n):
            prefixXor[i]=prefixXor[i-1]^arr[i] if i>=1 else arr[i]
        for i in range(m):
            l,r=queries[i]
            ans.append(prefixXor[r]^prefixXor[l-1] if l>=1 else prefixXor[r])
        return ans