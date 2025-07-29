class Solution:
    def solution_172_1(self, num: int) -> bool:
        return num > 0 and not num &amp; (num - 1)  and len(bin(num)) % 2