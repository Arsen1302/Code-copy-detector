class Solution:
    def solution_1393_4(self, colors: str) -> bool:
        a_segs = colors.split("B") 
        b_segs = colors.split("A") 
        
        a_removal = 0
        for seg in a_segs:
            if len(seg) > 2:
                a_removal += len(seg) - 2
        b_removal = 0
        for seg in b_segs:
            if len(seg) > 2:
                b_removal += len(seg) - 2
        return a_removal > b_removal