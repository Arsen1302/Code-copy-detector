class Solution:
    def solution_860_4(self, s: str) -> str:
        out = []
        res=[]
        i= 0 
        while i <len(s)-2: 
            if s[i+2] == "#":
                out.append(s[i:i+2]+"#")
                i+=3
            else:
                out.append(s[i])
                i+=1
        out.append(s[i:])
        for i in out :
            if "#"in i :
                res.append(chr(ord("a")+(int(i[:-1])-1)))
            else:
                for j in i:
                    res.append(chr(ord("a")+int(j)-1))
        return "".join(res)