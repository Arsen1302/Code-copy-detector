class Solution:
    def solution_1265_1(self, s: str) -> str:
        arr = [i[-1] + i[:-1] for i in s.split()]
        
        arr.sort()
        
        ans = ""
        for i in arr:
            ans += i[1:] + ' '
        
        return ans[:-1]