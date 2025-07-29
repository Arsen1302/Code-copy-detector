class Solution:
    def solution_1393_3(self, colors: str) -> bool:
        diff = 0 
        for k, grp in groupby(colors): 
            if k == "A": diff += max(0, len(list(grp)) - 2)
            else: diff -= max(0, len(list(grp)) - 2)
        return diff > 0