class Solution:
    def solution_873_1(self, s: str) -> List[str]:
        
        
        st=0 # track of index to take element from each word 
        s=s.split()
        ans=[]
        y=0
        for i in s:
            y=max(y,len(i))
   
        while st<y:
            u=[]
            for i in s:
                if st<len(i):
                    u.append(i[st])
                else:
                    u.append(' ')# adding spaces if word length is less
                    
            
            while u[-1]==' ': # using stack operation to remove trailing spaces
                u.pop()
            ans.append(''.join(u))
            st+=1# increasing index at each iteration 
        return ans