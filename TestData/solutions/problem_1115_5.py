class Solution:
    def solution_1115_5(self, code: List[int], k: int) -> List[int]:
        
        if k>0:
            code+=code[:k]
            
            for i in range(len(code)-k):
                summ=0
                
                for j in range(i+1,i+k+1):
                    summ+=code[j]
                code[i]=summ
            
            for i in range(k):
                code.pop()
                
        elif k<0:
            code=code[len(code)-abs(k):]+code
            
            for i in range(len(code)-1,abs(k)-1,-1):
                summ=0
                
                for j in range(i-abs(k),i):
                    summ+=code[j]
                code[i]=summ
            
            for i in range(abs(k)):
                code.pop(0)
                
        else:
            
            for i in range(len(code)):
                code[i]=0
        
        return code