class Solution:
    def solution_1272_5(self, s: str) -> bool:
        one_seg = sorted(s.split("0"), key=len)
        zero_seg = sorted(s.split("1"), key=len)
        return len(one_seg[-1]) > len(zero_seg[-1])