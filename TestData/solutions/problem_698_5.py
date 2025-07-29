class Solution:
    def solution_698_5(self, nums: List[int]) -> List[bool]:
        s = ''
        res = []
        for i in nums:
            s += str(i)
            decimal = int(s , 2)
            if decimal % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res