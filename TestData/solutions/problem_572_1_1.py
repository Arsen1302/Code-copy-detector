class Solution:
    def solution_572_1_1(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        left, right = cStart, cStart+1
        top, bottom = rStart, rStart+1
        current = 1
        move = 0
        while current <= rows*cols:
            # fill top
            for i in range(left+move, right+1):
                if self.solution_572_1_2(top, i, rows, cols):
                    ans.append([top, i])
                    current += 1
            left -= 1
            # fill right
            for i in range(top+1, bottom+1):
                if self.solution_572_1_2(i, right, rows, cols):
                    ans.append([i, right])
                    current += 1
            top -= 1
            # fill bottom
            for i in range(right-1, left-1, -1):
                if self.solution_572_1_2(bottom, i, rows, cols):
                    ans.append([bottom, i])
                    current += 1
            right += 1
            # fill left
            for i in range(bottom-1, top-1, -1):
                if self.solution_572_1_2(i, left, rows, cols):
                    ans.append([i, left])
                    current += 1
            bottom += 1
            move = 1
        return ans
    def solution_572_1_2(self, r, c, rows, cols):
        return 0<=r<rows and 0<=c<cols