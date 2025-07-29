class Solution:
    def solution_638_3(self, c, n) :
        return self.solution_638_3([0, c[0]==c[2], c[1]==c[3], c[2]==c[4], c[3]==c[5], c[4]==c[6], c[5]==c[7], 0], (n-1)%14) if n else [int(i) for i in c]