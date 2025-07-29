class Solution(object):
    def solution_524_2_1(self, rec1, rec2):
        # TIME and SPACE Complexity: O(1)
		
        #Funtion checking if coordinate of Rec2 overlapped Rec1;
        def solution_524_2_2(rec1_left, rec1_right, rec2_left, rec2_right):
            
            rec2_StartingCoordinate = max(rec1_left, rec2_left)
            rec1_EndingCoordinate = min(rec1_right, rec2_right)
            isOverlapped = rec2_StartingCoordinate < rec1_EndingCoordinate
            
            return isOverlapped
        
        
        #All Horizontal coordinates of Rec1 and Rec2;
        rec1HozlLeft = rec1[0]
        rec1HozlRight = rec1[2]
        rec2HozlLeft = rec2[0]
        rec2HozlRight = rec2[2]
        
        #All Vertical coordinates of Rec1 and Rec2;
        rec1VerBottom = rec1[1]
        rec1VerTop = rec1[3]
        rec2VerBottom = rec2[1]
        rec2VerTop = rec2[3]
        
        # 1st Check the Horizontal coordinates if Rec2 is overlapped Rec1;
        ## 2nd Check the Vertical coordinates if Rec2 is Overlapped Rec1; 
        ### return True if both Horizontal and Vertical are Overlapped
        return solution_524_2_2(rec1HozlLeft, rec1HozlRight, rec2HozlLeft, rec2HozlRight) and \
                solution_524_2_2(rec1VerBottom, rec1VerTop, rec2VerBottom, rec2VerTop)