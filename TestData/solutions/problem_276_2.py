class Solution:
    def solution_276_2(self, s: str, k: int) -> str:
        s = (s.upper()).replace("-","")[::-1]
        ans = str()
        for i in range(0,len(s),k):
            ans += s[i:i+k]+"-"
        return ans[::-1][1:]