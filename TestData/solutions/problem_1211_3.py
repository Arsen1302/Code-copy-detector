class Solution:
    def solution_1211_3(self, s: str) -> int:
        final=[]
        sums=0
        for i in range(len(s)):
            temp=""
            for j in range(i,len(s)):
                temp+=s[j]
                final.append(temp)        
        for i in final:
            values=(Counter(i)).values()
            sums+= max(values)-min(values)
        return(sums)