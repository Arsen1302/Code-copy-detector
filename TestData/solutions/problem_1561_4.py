class Solution:
    def solution_1561_4(self, num: str) -> str:
        ss = 0
        res=''
        for i in set(num):
            if i*3 in num:
                if ss <= int(i):
                    ss = int(i)
                    res=i*3
        return res