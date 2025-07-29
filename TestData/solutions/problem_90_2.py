class Solution:
    def solution_90_2(self, left: int, right: int) -> int:
        leftb = "{0:b}".format(left)
        rightb = "{0:b}".format(right)
        
        if len(rightb) > len(leftb):
            return 0
        
        res = left
        for i in range(left + 1, right + 1):
            res = res &amp; i
        
        return res