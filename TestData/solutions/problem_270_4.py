class Solution:
    def solution_270_4(self, num: int) -> int:
        return num^int('1'*len(bin(num)[2:]), 2)