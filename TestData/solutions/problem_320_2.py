class Solution:
    def solution_320_2(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            if len(s[i:i+k])<k:
                s[i:i+k]=s[i:i+k][::-1]
            elif 2*k>len(s[i:i+k])>=k:
                s[i:i+k]=s[i:i+k][::-1]
        return "".join(s)