class Solution:
    def solution_923_1_1(self,num):
        p=0
        while(num!=1):
            if num%2==0:
                num=num//2
                
            else:
                num=(3*num)+1
            p+=1
            
        return p
             
    def solution_923_1_2(self, lo: int, hi: int, k: int) -> int:
        
        temp=sorted(range(lo,hi+1),key=lambda x:self.solution_923_1_1(x))
        return temp[k-1]
		```