class Solution:
    def solution_1329_2_1(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        
        score = [[0]*m for _ in range(m)]
        for i in range(m): 
            for j in range(m): 
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        
        @cache 
        def solution_1329_2_2(mask, j): 
            """Return max score of assigning students in mask to first j mentors."""
            ans = 0 
            for i in range(m): 
                if not mask &amp; (1<<i): 
                    ans = max(ans, solution_1329_2_2(mask^(1<<i), j-1) + score[i][j])
            return ans 
        
        return solution_1329_2_2(1<<m, m-1)