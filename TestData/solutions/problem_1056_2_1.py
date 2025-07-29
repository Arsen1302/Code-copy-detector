class Solution:
    def solution_1056_2_1(self, stoneValue: List[int]) -> int:
        def solution_1056_2_2(start, end):
            if start >= end:
                return 0
            max_score = 0
            # divides the array into [start,cut] and 
            # [cur+1, end]
            for cut in range(start, end):
                sum1 = partial_sum[start][cut]
                sum2 = partial_sum[cut+1][end]
                # remaing part is [cut+1, end]
                if sum1 > sum2:
                    score = sum2+solution_1056_2_2(cut+1, end)
                # remaining part is [start, cut]
                elif sum1 < sum2:
                    score = sum1+solution_1056_2_2(start, cut)
                # two rows are equal
                else:
                    score = sum1+max(solution_1056_2_2(start, cut), solution_1056_2_2(cut+1, end))
                max_score = max(score, max_score)
            return max_score
                
        
        def solution_1056_2_3():
            for i in range(n):
                partial_sum[i][i] = stoneValue[i]
            for i in range(n):
                for j in range(i+1, n):
                    partial_sum[i][j] = partial_sum[i][j-1]+stoneValue[j]
                               
            
        n = len(stoneValue)
        partial_sum = [[0]*n for _ in range(n)]
        solution_1056_2_3()
        return solution_1056_2_2(0, n-1)