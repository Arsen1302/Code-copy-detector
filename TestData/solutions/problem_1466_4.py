class Solution:
    def solution_1466_4(self, s: List[str], t: List[str]) -> int:
        
        d={}
        for i in s:
            x = "".join(sorted(i))
            d[x] = 1
        
        ans=0
        for i in t:
            i = "".join(sorted(i))
            for j in range(len(i)):
                x = i[:j]+i[j+1:]
                if x in d:
                    ans+=1
                    break
        return ans