class Solution:
    def solution_1557_3(self, number: str, digit: str) -> str:
        l=[]
        for i in range(len(number)):
            if number[i]==digit:
                l.append(int(number[:i]+number[i+1:]))
        return str(max(l))