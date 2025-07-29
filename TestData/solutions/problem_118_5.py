class Solution:
    def solution_118_5(self, n: int) -> int:
        if n < 0: return 0 #edge case 
        
        #number of 1's in n where 0 <= n <= x*10**i
        fn = lambda k, i: k*i*10**(i-1) + (k==1) + (k>1)*10**i
        
        ans = val = i = 0
        while n:
            n, x = divmod(n, 10)
            ans += fn(x, i) + (x==1)*val
            val += x*10**i
            i += 1
        return int(ans)