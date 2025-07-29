class Solution:
    def solution_1289_3(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = [False] * 51 
        for start, end in ranges: 
            for x in range(start, end+1): 
                cover[x] = True 
        return all(cover[x] for x in range(left, right+1))