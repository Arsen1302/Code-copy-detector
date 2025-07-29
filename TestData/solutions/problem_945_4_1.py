class Solution:
    def solution_945_4_1(self, k):
        if k < 2:
            return k
        n1, n2 = 1, 1
        while n2 <= k:
            n2, n1 = n1+n2, n2
        return self.solution_945_4_1(k - n1) + 1
    
    def solution_945_4_2(self, k: int) -> int:
        return self.solution_945_4_1(k)