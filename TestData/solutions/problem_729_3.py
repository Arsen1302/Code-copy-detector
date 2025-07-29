class Solution:
    def solution_729_3(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        res = 0
        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
        sum1 = 0        
        for i in range(minutes):
            if grumpy[i] == 1:
                sum1 += customers[i]
                
        result = sum1
        for r in range(minutes, n):
            if grumpy[r] == 1:
                sum1 += customers[r]
            if grumpy[r - minutes] == 1:
                sum1 -= customers[r - minutes]
            result = max(sum1, result)
        
        return res + result