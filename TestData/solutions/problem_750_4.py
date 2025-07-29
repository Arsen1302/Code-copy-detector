class Solution:
    def solution_750_4(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [float('inf')] * (len(books)+1)
        dp[0] = 0
        for i in range(len(books)):
            w, h = 0, 0
            for j in range(i, len(books)):
                w += books[j][0]
                h = max(h, books[j][1])
                
                if w <= shelf_width:
                    dp[j+1] = min(dp[j+1], dp[i] + h)
                else:
                    break
        
        return dp[len(books)]