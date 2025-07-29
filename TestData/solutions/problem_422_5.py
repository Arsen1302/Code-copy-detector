class Solution:
    def solution_422_5(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        table = [[0 for x in range(n+1)] for x in range(m+1)]

        total = 0
        Flag = True
        for i in range(1,m+1):
            total+=ord(s1[i-1])
            for j in range(1,n+1):
                if(Flag):
                    total+=ord(s2[j-1])
                    
                if(s1[i-1]==s2[j-1]):
                    table[i][j] = max(table[i-1][j],table[i][j-1],table[i-1][j-1]+ord(s1[i-1]))
                else:
                    table[i][j] = max(table[i-1][j],table[i][j-1])
            Flag = False
        
        return total-table[-1][-1]*2