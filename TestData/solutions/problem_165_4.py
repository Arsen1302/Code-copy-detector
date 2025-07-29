class Solution:
    def solution_165_4(self, p: str) -> bool:
        i=0
        st=1
        lst=p.split(",")
        while(i<len(lst)):
            st-=1
            if st<0:
                return False
            if lst[i]!="#": 
                st+=2
            i=i+1
        
        if st==0:
            return True
        else:
            return False