class Solution:
    def solution_1460_4(self, title: str) -> str:
        sfin = title.split(' ')
        res=[]
        s=''
        for i in sfin:
            if len(i)<=2:
                s=i.lower()
            elif sfin[0][0].islower() or sfin[0][0].isupper():
                s=i[0][0].upper()
                s+=i[1:].lower()
            res.append(s)
        return ' '.join(res)