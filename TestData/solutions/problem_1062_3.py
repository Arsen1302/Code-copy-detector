class Solution:
    def solution_1062_3(self, s: str) -> int:
        cnt, n = 0, len(s)
        mod = 10**9 + 7
        
        for i in range(n):
            if s[i] == '1':
                cnt += 1
        
        if cnt%3 != 0:
            return 0
        if cnt == 0:
            return (n-1)*(n-2)//2 % (mod)
        
        parts = cnt // 3
        left, val1, i = 0, 0, 0
        while i < n:
            if s[i] == '1':
                left += 1
            i += 1
            if left == parts:
                while i < n and s[i] == '0':
                    val1 += 1
                    i += 1
                break
        
        right, val2, i = 0, 0, n-1
        while i >= 0:
            if s[i] == '1':
                right += 1
            i -= 1
            if right == parts:
                while i >= 0 and s[i] == '0':
                    val2 += 1
                    i -= 1
                break
        
        return (val1+1)*(val2+1) % (mod)