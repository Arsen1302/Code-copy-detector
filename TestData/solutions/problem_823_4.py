class Solution:
    def solution_823_4(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        # first set all the ones where there is a two in the col sum
        mat = [[0]*len(colsum), [0]*len(colsum)]

        # go over the colsums and place the ones
        for idx, num in enumerate(colsum):

            # we have to place both of them
            if num == 2:
                mat[0][idx] = 1
                mat[1][idx] = 1
                upper -= 1
                lower -= 1
            
            # we only place one and do that greedily
            # by selecting the higher count
            elif num == 1:
                if lower > upper:
                    mat[1][idx] = 1
                    lower -= 1
                else:
                    mat[0][idx] = 1
                    upper -= 1
            
            # make a check whether we used too much ones
            if lower < 0 or upper < 0:
                return []
        
        return mat if lower == 0 and upper == 0 else []