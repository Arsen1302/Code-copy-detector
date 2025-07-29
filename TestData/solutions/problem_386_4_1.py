class Solution:
    def solution_386_4_1(self, img: List[List[int]]) -> List[List[int]]:
        if len(img) == 1 and len(img[0]) == 1:
            return img
        for row in range(len(img)):
            for col in range(len(img[0])):
                partial = self.solution_386_4_2(img, row, col)
                partial <<= 8
                img[row][col] += partial
        
        for row in range(len(img)):
            for col in range(len(img[0])):
                img[row][col] >>= 8
        
        return img
    
    def solution_386_4_2(self, m: List[List[int]], r: int, c: int) -> int:
        directions = [(0,0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        ans = 0
        times = 0
        for dx, dy in directions:
            if r + dx >= 0 and r + dx < len(m) and c + dy >= 0 and c + dy < len(m[0]):
                times += 1
                ans += (m[r+dx][c+dy] &amp; 255)
        return int(ans / times)