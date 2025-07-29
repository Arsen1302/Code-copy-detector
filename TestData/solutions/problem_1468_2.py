class Solution:
    def solution_1468_2(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k): 
            ss = s[i:i+k]
            ans.append(ss + (k-len(ss))*fill)
        return ans