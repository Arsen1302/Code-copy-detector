class Solution:
    def solution_1533_2(self, s: str, c: str) -> int:
        dif=(int(c[:2])*60+int(c[3:]))-(int(s[:2])*60+int(s[3:]))
        count=0
        print(dif)
        arr=[60,15,5,1]
        for x in arr:
            count+=dif//x
            dif=dif%x
        return count