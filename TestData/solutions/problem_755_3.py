class Solution:
    def solution_755_3(self, seq: str) -> List[int]:
        
        
        
        ans=[]
        la=0
        lb=0
        
        for i in range(len(seq)):
            
            if seq[i]=='(':
                
                if la > lb:
                    lb+=1
                    ans.append(0)
                elif lb>la:
                    la+=1
                    ans.append(1)
                else:
                    la+=1
                    ans.append(1)
            else:
                if la >0:
                    ans.append(1)
                    la-=1
                elif lb>0:
                    ans.append(0)
                    lb-=1
        return ans