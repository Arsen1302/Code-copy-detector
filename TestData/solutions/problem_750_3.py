class Solution:
    def solution_750_3(self, books: List[List[int]], shelfWidth: int) -> int:
        books = [[0,0]] + books
        dp = [float("inf")] * len(books)
        dp[0] = 0 
        for i in range(1,len(books)):
            width, height = books[i]
            j = i
            while width <= shelfWidth and j>0:
                dp[i] = min(dp[i], dp[j-1]+height)
                j -= 1 
                width += books[j][0]
                height = max(height, books[j][1])
        #print(dp)
        return dp[-1]