class Solution:
    def solution_1259_3_1(self, num: str, k: int) -> int:
        #find kth
		target=num
        for i in range(k):
            target=self.solution_1259_3_2(target)
        
		#count step
        res=0
        num=list(num)
        for i in range(len(num)):
            if num[i]!=target[i]:
                j=i
				#num[j]==target[i]
                while num[j]!=target[i]:
                    j+=1
				#swap (j-i) times
                while j>i:
                    num[j-1],num[j]=num[j],num[j-1]
                    res+=1
                    j-=1
        return res                    
        
    def solution_1259_3_2(self,num):
        num=list(num)
        
        # find first non-ascending digit num[i-1] from right to left
        i=len(num)-1
        while i>0 and num[i-1]>=num[i]:
            i-=1
            
        # find first larger digit num[j] from right to left
        if i>0:
            for j in range(len(num)-1,i-1,-1):
                if num[j]>num[i-1]:
                    break        
        #swap
        num[i-1],num[j]=num[j],num[i-1]
        
        #reverse
        return ''.join(num[:i]+sorted(num[i:]))