class Solution:
    def solution_1323_4(self, s: str) -> bool:
        dicta={}
        for i in s:
            dicta[i]=s.count(i)
        d=dicta[s[0]]
        print(d)
        for i,j in enumerate(dicta):
            print(j)
            if dicta[j]!=d:
                return False
        return True