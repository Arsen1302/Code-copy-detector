class Solution:
    def solution_811_3(self, folder: List[str]) -> List[str]:
        ans = []
        for x in sorted(folder): 
            if not ans or not x.startswith(ans[-1]+"/"): 
                ans.append(x)
        return ans