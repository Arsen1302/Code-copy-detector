class Solution:
    def solution_807_4_1(self, n: int, rollMax: List[int]) -> int:
        dp = {}
        def solution_807_4_2(n,last,count):
            if n == 0: return 1
            if (n,last,count) in dp: return dp[(n,last,count)]
            ans = 0
            for i in range(6):
                if last == i:
                    if count == rollMax[i]: continue
                    ans += solution_807_4_2(n-1,last,count + 1)
                else:
                    ans += solution_807_4_2(n-1,i,1)
            dp[(n,last,count)] = ans
            return ans
        
        return solution_807_4_2(n,None,0) % 1000000007