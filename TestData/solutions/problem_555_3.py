class Solution:
    def solution_555_3(self, n: int) -> int:
        t=bin(n).replace('0b','')
        if t.count('1')<2:
            m= 0
        else:
            r=[]
            for i in range(len(t)):
                if t[i] == '1':
                    r+=[i]
            m=abs(r[0]-r[1])
            for i in range(1,len(r)-1):
                if m < abs(r[i]-r[i+1]):
                    m=abs(r[i]-r[i+1])
        return m