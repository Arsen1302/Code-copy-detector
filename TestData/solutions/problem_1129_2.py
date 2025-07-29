class Solution:
    def solution_1129_2(self, accounts: List[List[int]]) -> int:
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)
```easy solution using python basics