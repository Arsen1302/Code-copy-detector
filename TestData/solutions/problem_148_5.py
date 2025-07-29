class Solution:
    def solution_148_5(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n//2+1):
            x = num[:i]
            if x.startswith("0") and len(x) > 1: break #no leading zero 
            for j in range(i+1, min(n-i, (n+i)//2)+1): #i <= n-j and j-i <= n-j
                yy = num[i:j]
                if yy.startswith("0") and len(yy) > 1: break #no leading zero
                
                ii, xx = i, x
                while num.startswith(yy, ii):
                    ii += len(yy)
                    xx, yy = yy, str(int(xx) + int(yy))
                if ii == len(num): return True 
                
        return False