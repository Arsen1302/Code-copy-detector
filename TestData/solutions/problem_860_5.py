class Solution:
    def solution_860_5(self, s: str) -> str:
        res=[]
        i= 0 
        while i <len(s): 
            if i + 2 < len(s)  and s[i+2] == "#" :
                res.append(chr(int(s[i:i + 2]) + 96)) 
                i+=3
              
            else:
                res.append(chr(96+int(s[i])))
                i+=1

        return "".join(res)