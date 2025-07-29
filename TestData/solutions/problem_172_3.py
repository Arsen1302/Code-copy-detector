class Solution:
    def solution_172_3(self, n: int) -> bool:
        epsilon = 0.0000000001
        if not n > 0:
            return False
        logged = (math.log(abs(n), 4))%1
        if (logged < epsilon or logged > 1 - epsilon):
            return True