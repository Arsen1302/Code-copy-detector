class Solution:
    def solution_216_5(self, num: int) -> str:
        # d = {}
        # for i in range(16):
        #     if i < 10:
        #         d[i] = str(i)
        #     if i == 10:
        #         d[i] = 'a'
        #     elif i > 10:
        #         d[i] = chr(ord(d[i-1])+1)
        d = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if num < 0:
            num = abs(num)
            num = 2**32 - num
        if num == 0:
            return '0'
        res = ''
        while num > 0:
            res = d[num%16] + res
            num //= 16
        return res