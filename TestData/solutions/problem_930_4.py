class Solution:
    def solution_930_4(self, rating: List[int]) -> int:
        ans = 0
        seen = [[0]*2 for _ in rating]
        for i in range(len(rating)): 
            for ii in range(i): 
                if rating[ii] < rating[i]: 
                    ans += seen[ii][0]
                    seen[i][0] += 1
                elif rating[ii] > rating[i]: 
                    ans += seen[ii][1]
                    seen[i][1] += 1
        return ans