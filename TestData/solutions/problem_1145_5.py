class Solution:
    def solution_1145_5(self, number: str) -> str:
        number = ''.join(number.split('-'))
        number = ''.join(number.split())
        if len(number)<=3:
            return number
        if len(number) == 4:
            return number[:2]+'-'+number[2:]
        i = 0
        s = ''
        while(i<len(number)):
            s += number[i:i+3]+'-'
            i += 3
            if len(number)-(i)<=4:
                if len(number)-(i) == 4:
                    return s+number[i:(i+2)]+'-'+number[(i+2):]
                return s+number[i:]
        return s[:-1]