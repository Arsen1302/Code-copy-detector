class Solution:
    def solution_1193_4(self, s: str) -> int:
        n = len(s)
        print(n)
        x1 = ''
        x2 = ''
        l = []
        if n % 2 == 0:
            x1 = '10'*(n//2)
            x2 = '01'*(n//2)
        else:
            x1 = '10'*(n//2)+'1'
            x2 = '01'*(n//2)+'0'
        l = [x1,x2]
        count1, count2 = 0,0
        for i in range(len(s)):
            if l[0][i] != s[i]:
                count1 += 1
            if l[1][i] != s[i]:
                count2 += 1
        return min(count1, count2)