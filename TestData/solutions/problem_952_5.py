class Solution:
    def solution_952_5(self, s: str) -> int:
        
        no1=0
        rez=0
        
        for i in s:  #here we count the 1's like everything is on the left side 
            if i=="1":
                no1+=1
        cur=no1   
        for i in range(len(s)-1):  #here we expand the right side
            if  s[i]=="0":  #when we find a 0 we sum1 !len(s)-1 because the none parts can be empty
                cur+=1
            else:  #when we find a 1 we lower the current because it means the 1 isn't in the left side anymore
                cur-=1
            if cur>rez: # we update the rez if needed
                rez=cur
        return rez