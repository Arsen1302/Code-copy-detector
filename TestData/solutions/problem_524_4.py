class Solution:
    def solution_524_4(self, rec1: List[int], rec2: List[int]) -> bool:
        # 0) Make sure rec2 is always on the right of rec1 for simplicity
        if rec1[2] > rec2[2]:
            rec1, rec2 = rec2, rec1
            
        # 1) All reasons that cause overlap to be impossible
        #    - The whole rec2 is on the right side of rec1
        #    - The whole rec2 is on the top side of rec1
        #    - The whole rec2 is on the bottom side of rec1
        if rec2[0] >= rec1[2] or \
           rec2[1] >= rec1[3] or \
           rec2[3] <= rec1[1]:      
            return False
        
        return True