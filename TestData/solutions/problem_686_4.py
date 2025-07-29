class Solution:
    def solution_686_4(self, n: int) -> int:
        res=""
        j=-1
        for i in range(n,0,-1):
            res+=str(i)
            j+=1
            if j <n-1:
                if j%4==0 :
                    res+="*"
                elif j%4==1:
                    res+="//"
                elif j%4==2:
                    res+="+"
                elif j%4==3:
                    res+="-"
        return (eval(res))