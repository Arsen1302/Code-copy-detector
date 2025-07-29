class Solution:
    def solution_497_3_1(self, s: str, words: List[str]) -> int:
        res=[]
        
        for word in words:
            res.append(self.solution_497_3_2(s,word))
        print(res)
        return sum(res)
    
    def solution_497_3_2(self,s,x):
            i = j = 0
            while i < len(s) and j < len(x):
                counts = 1
                while i<len(s)-1 and s[i]==s[i+1]:
                    i+=1
                    counts+=1
                countx = 1
                while j<len(x)-1 and x[j]==x[j+1]:
                    j+=1
                    countx+=1
                if s[i]!=x[j]: 
                    return 0
                i+=1
                j+=1
                if counts<countx:
                    return 0
                if countx==counts: continue
                if counts<=2: 
                    return 0
            return 1 if i>=len(s) and j>=len(x) else 0