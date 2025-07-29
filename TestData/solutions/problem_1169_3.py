class Solution:
    def solution_1169_3(self, rectangles: List[List[int]]) -> int:
        max_size = 0
        max_count = 0 
        for rect in rectangles:
            sq_size = min(rect[0], rect[1])
            if sq_size > max_size:
                max_size = sq_size
                max_count = 1
            elif sq_size == max_size:
                max_count+=1
        
        return max_count