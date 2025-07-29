class Solution:
    def solution_755_2(self, seq: str) -> List[int]:
        m,c,n=0,0,len(seq)
        for i in range(n):
            if seq[i]=='(':
                c+=1
                m=max(c,m) # Here m is the maximium depth of the VPS
            elif seq[i]==')': 
                c-=1
        a=[]
        m//=2 # Minimum depth possible by breaking string in two parts A and B
        for i in range(n):
            if seq[i]=='(':
                c+=1
                if c<=m:
                    a.append(0) #For A
                else:
                    a.append(1) #For B
            else:
                if c<=m:
                    a.append(0)
                else:
                    a.append(1)
                c-=1
        return a