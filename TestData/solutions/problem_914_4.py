class Solution:
    def solution_914_4(self, flips: List[int]) -> int:
        s,maxi,res = 0,0,0
        for i in flips:
            if i > maxi:
                maxi = i
            s += i
            if s == (maxi * (maxi+1))//2:
                res +=1
        return res