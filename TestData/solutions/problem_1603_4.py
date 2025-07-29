class Solution:
    def solution_1603_4(self, n: int) -> int:
        dpArray = [0]*(n + 1)
        dpArray[0] = 1
        dpArray[1] = 2
        
        mod = 10**9 + 7
        
        for i in range(2, n + 1):
            dpArray[i] = dpArray[i - 1] + dpArray[i - 2]
            dpArray[i] = dpArray[i] % mod
            
        return (dpArray[n]**2) % mod