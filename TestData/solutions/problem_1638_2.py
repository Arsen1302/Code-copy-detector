class Solution:
    def solution_1638_2(self, s: str, k: int) -> int:
        
        # For storing the largest substring ending at that character 
        psum=[0]*26
        ans=1
        for i in range(len(s)):
            element=ord(s[i])-97
            
            # Checking for k characters left to current element i.e. 2 characters left to c will be 'a' and 'b'  
            
            j=element
            while j>-1 and j>=element-k:
                psum[element]=max(psum[element],psum[j]+1)
                j-=1
                
            # Checking for k characters right to current element i.e. 2 characters left to c will be 'd' and 'e'     
                
            j=element+1
            while j<26 and j<=element+k:
                psum[element]=max(psum[element],psum[j]+1)
                j+=1
                
            ans=max(ans,psum[element])
        return ans