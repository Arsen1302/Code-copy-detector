class Solution:
    def solution_478_5(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            p = ''
            if '3' in str(i) or '4' in str(i) or '7' in str(i):
                continue
            for j in str(i):
                if j == '0':
                    p += '0'
                elif j == '1':
                    p += '1'
                elif j == '8':
                    p += '8'
                
                elif j == '2':
                    p += '5'
                elif j == '5':
                    p += '2'
                
                elif j == '6':
                    p += '9'
                elif j == '9':
                    p += '6'
                    
            if p != str(i):
                ans += 1
        
        return ans