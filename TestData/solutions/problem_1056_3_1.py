class Solution:
    def solution_1056_3_1(self, stoneValue: List[int]) -> int:
        def solution_1056_3_2():
            for i in range(n):
                partial_sum[i][i] = stoneValue[i]
            for i in range(n):
                for j in range(i+1, n):
                    partial_sum[i][j] = partial_sum[i][j-1]+stoneValue[j]
                               
        # (O(n) search)    
        def solution_1056_3_3():
            # based on the fact that cut index is increasing with k for 
            # partial_sum[start][k]
            for i in range(n-1):
                cp = i
                cut_index[i][i+1] = i
                for j in range(i+2, n):
                    while cp < j-1 and partial_sum[i][cp] < partial_sum[cp+1][j]:
                        cp += 1  
                    cut_index[i][j] = cp
		
			
        @lru_cache(None)
        def solution_1056_3_4(start, end):
            if start >= end:
                return 0
            max_score = 0
            # find first cut s.t. left sum >= right sum 
            cut = cut_index[start][end]
            # we can't find cut s.t. left sum >= right sum
            if cut == -1:
                cut = end-1
            sum1 = partial_sum[start][cut]
            sum2 = partial_sum[cut+1][end]
            if sum1 < sum2:
                # calcuate left[start][cut] if not yet
                solution_1056_3_4(start, cut)
                # the remaining will be the left part for sure, no 
                # matter where the cut is. 
                max_score = left[start][cut]
            elif sum1 == sum2:
                solution_1056_3_4(start, cut)
                solution_1056_3_4(cut+1, end)
                # if real cut in the range of [cut+1, end], remaining will be the right part
                # if real cut in the range of [0, cut], remaing will be the left part
                # if real cut is cut, either can be the remaining. 
                max_score = max(left[start][cut], right[cut+1][end])
            else:
                solution_1056_3_4(cut+1, end)
                # we are selecting the cut in the range of [cut, end] having 
                # the max score. For cut in that range, the remaining is 
                # the right part of the cut for sure. 
                max_score = right[cut+1][end]
                if cut > start:
                    solution_1056_3_4(start, cut-1)
                    # we are selecting the cut in the range of [0, cut] having 
                    # the max score. The remaining is the left part for sure. 
                    max_score = max(max_score, left[start][cut-1])
            solution_1056_3_4(start, end-1)
            solution_1056_3_4(start+1, end)
            # updating left and right arrays. 
            left[start][end] = max(left[start][end-1], partial_sum[start][end]+max_score)
            right[start][end] = max(right[start+1][end], partial_sum[start][end]+max_score)
            return max_score
            
        n = len(stoneValue)
        partial_sum = [[0]*n for _ in range(n)]
        cut_index = [[-1]*n for _ in range(n)]
        # left[i][j]: cut in the range of [i, j], max score of left part
        # right[i][j]: cut in the range of [i, j], max score of right part
        left = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]
        for i in range(n):
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]
        solution_1056_3_2()
        # for partial_sum[i][j], find cut index between i and j 
        # s.t partial_sum[i][cut_index] >= partial_sum[cut_index+1][j] or 
        # cut_index = j-1 if not exist. 
        solution_1056_3_3()
        return solution_1056_3_4(0, n-1)