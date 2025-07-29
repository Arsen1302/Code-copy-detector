class Solution:

    def solution_900_3(self, n: int) -> int:

        if n == 1:
            return 1 # Only way to pickup and deliver 1 order
        
        return int(((2*n *(2*n-1))/2 * self.solution_900_3(n-1))%(10**9 + 7))