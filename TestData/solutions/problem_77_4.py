class Solution:
    def solution_77_4(self, columnTitle: str) -> int:
        
        p = 1
        summ = 0
        for i in columnTitle[::-1] :
            summ += p*(ord(i)-64)        # -ord(A)+1
            p*= 26
        
        return summ