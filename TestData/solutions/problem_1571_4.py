class Solution:
    def solution_1571_4(self, candidates: List[int]) -> int:
        d = {}
        for i in range(32):
            d[i] = 0 
        for a in candidates:
            x = bin(a)[2:][::-1]
            for j in range(len(x)):
                if x[j]=='1':
                    d[j]+=1
        return max(d.values())