class Solution:
    def solution_456_5_1(self, left: int, right: int) -> int:
        def solution_456_5_2(num):
            return bin(num).count("1")
        
        def solution_456_5_3(bits):
            return bits in [2,3,5,7,11,13,17,19]
        
        ans = 0
        for num in range(left,right+1):
            ans += 1 if solution_456_5_3(solution_456_5_2(num)) else 0
        return ans