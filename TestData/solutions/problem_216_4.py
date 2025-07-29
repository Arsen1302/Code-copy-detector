class Solution:
    def solution_216_4(self, num: int) -> str:
        
        return "{0:x}".format(num) if num >= 0 else "{0:x}".format(num + 2 ** 32)