class Solution:
    def solution_236_3(self, s: str) -> int:
        if s=="":
            return(0)
        j = s.split(" ")
        print(j)
        c=0
        for it in j:
            if it!="":
                c+=1
        return(c)