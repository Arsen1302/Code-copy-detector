class Solution:
    def solution_750_2_1(self, idx , n , height , width):
        if idx == n:return height
        
        if (idx,height,width) in self.dp: return self.dp[(idx,height,width)]
        
        choice1 = self.solution_750_2_1(idx+1,n,max(self.books[idx][1],height), width - self.books[idx][0])\
        if width >= self.books[idx][0] else float('inf')
        
        choice2 = self.solution_750_2_1(idx+1,n,self.books[idx][1], self.shelfWidth - self.books[idx][0]) + height
        
        ans = min(choice1,choice2)
        self.dp[(idx,height,width)] = ans
        return ans
    
    def solution_750_2_2(self, books: List[List[int]], shelfWidth: int) -> int:
        self.books = books
        self.shelfWidth = shelfWidth
        self.dp = {}
        return self.solution_750_2_1(0,len(books),0,shelfWidth)