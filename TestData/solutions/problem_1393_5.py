class Solution:
    def solution_1393_5(self, colors: str) -> bool:
        
        acount=0
        bcount=0
        
        for i in range(len(colors)):
            c=colors[i]
            if(c=='A' and i-1>=0 and i+1<len(colors) and colors[i-1]=='A' and colors[i+1]=='A'):
                acount+=1
            if(c=='B' and i-1>=0 and i+1<len(colors) and colors[i-1]=='B' and colors[i+1]=='B'):
                bcount+=1
                
        if(acount<=bcount):
            return False
        else:
            return True