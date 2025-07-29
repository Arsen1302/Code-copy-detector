class Solution:
    def solution_1470_5(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        h = []    # (point, idx)
        candi = []  # (idx, point)

        
        for i in range(n):
            while candi: # we have candidates
                if candi[0][0] < i:  # this means the current i bigger than the right bound of the candidate which has the smallest bound
                    idx, point = heappop(candi)
                    heappush(h, (point, idx))
                else: 
                    break
                    
            if h:
                point, idx = h[0]  # h[0] is the highest points we can get from prevous questions, and we can access
                heappush(candi, (i + questions[i][1], point - questions[i][0]))
            else:
                heappush(candi, (i + questions[i][1], -questions[i][0]))


        r1 = -h[0][0] if h else 0
        r2 = max([-v[1] for v in candi]) if candi else 0
        
        return max(r1, r2)