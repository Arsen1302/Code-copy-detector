class Solution:
    def solution_733_4_1(self, matrix: List[List[int]]) -> int:
        def solution_733_4_2(alist):
            olist = []
            for v in alist:
                olist.append(0 if v else 1)
                
            return tuple(olist)
        
        complementary_row_dict = {}
        for row in matrix:            
            if not row[0]:
                row = solution_733_4_2(row)
            else:
                row = tuple(row)
                
            complementary_row_dict[row] = complementary_row_dict.get(row, 0) + 1
            
        return max(complementary_row_dict.values())