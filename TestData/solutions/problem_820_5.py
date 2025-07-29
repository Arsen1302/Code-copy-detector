class Solution:
    def solution_820_5(self, s: str) -> str:
        
        ans=list()
        
        count_bracket=0
        
        for index,char in enumerate(s):
            if char =='(':
                count_bracket+=1
                
            elif char ==')':
                if not count_bracket:
                    continue
                
                count_bracket-=1
            
            ans.append(char)
          
        
        for i in range(len(ans)-1,-1,-1):
            if ans[i]=='(' and count_bracket >0 :
                ans[i]=''
                count_bracket-=1
            else:
                continue
                
        return ''.join(ans)