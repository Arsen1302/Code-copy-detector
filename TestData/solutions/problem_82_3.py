class Solution:
    def solution_82_3(self, s: str) -> List[str]:
        dna= {}
        m=[]
        for i in range(len(s) -9):
            x=s[i:i+10]
            if x in dna:
                dna[x]=dna[x]+1
                m.append(x)
            else:
                dna[x]= 1 
        return(list(set(m)))