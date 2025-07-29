class Solution:
def solution_536_3(self, s: str, shifts: List[int]) -> str:
    if len(shifts)>1:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]                 # Suffix sum
    
    res=""
    for i in range(len(s)):
        c = chr(((ord(s[i])+shifts[i]-ord("a"))%26)+ord("a"))
        res+=c
    
    return res