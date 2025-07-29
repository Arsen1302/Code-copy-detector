class Solution:
    def solution_512_2(self, S: str) -> str:
        out=''
        l=S.split()
        for i in range(len(l)):
            if l[i][0] in 'aeiouAEIOU':
                out+=l[i]+'m'+'a'*(i+2)+' '
            else:
                out+=l[i][1:]+l[i][0]+'m'+'a'*(i+2)+' '
        return out[:-1]