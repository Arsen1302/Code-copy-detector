class Solution:
def solution_205_2_1(self, s: str) -> str:       
    def solution_205_2_2(s,p):
        res = ""
        i,num = p,0
        while i<len(s):
            asc = (ord(s[i])-48)
            if 0<=asc<=9:           # can also be written as if s[i].isdigit()
                num=num*10+asc
            elif s[i]=="[":
                local,pos = solution_205_2_2(s,i+1)
                res+=local*num
                i=pos
                num=0
            elif s[i]=="]":
                return res,i
            else:
                res+=s[i]
            i+=1
        return res,i
    
    return solution_205_2_2(s,0)[0]