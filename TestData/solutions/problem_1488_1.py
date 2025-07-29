class Solution:
    def solution_1488_1(self, num: int) -> int:
        
        if num == 0 : return 0 
        snum = sorted(str(num))
        if snum[0] == '-' :
            return -int("".join(snum[:0:-1]))
        elif snum[0] == '0' :
            x = snum.count('0')
            return "".join([snum[x]]+['0'*x]+snum[x+1:])
        else :
            return "".join(snum)