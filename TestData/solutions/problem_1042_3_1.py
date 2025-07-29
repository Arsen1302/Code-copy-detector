class Solution:
    def solution_1042_3_1(self, n: int, k: int) -> str:
        s1 = '0'
        for i in range(1, n+1):
            a = self.solution_1042_3_2(s1)
            s1 = (s1 + '1' + a)
            a = s1
        return s1[k-1]

    def solution_1042_3_2(self, s):
        ans = ''
        for i in range(len(s)):
            if s[i] == '0':
                ans += '1'
            elif s[i] == '1':
                ans += '0'
        return ans[::-1]