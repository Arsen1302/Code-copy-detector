class Solution:
    def solution_689_4(self, n: int) -> int:
        return int(bin(n)[2:].replace('1', 'z').replace('0', '1').replace('z', '0'), 2)