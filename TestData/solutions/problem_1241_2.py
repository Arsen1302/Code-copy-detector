class Solution:
    def solution_1241_2(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        a, b, c = 1, 0, 1
        for i in range(1, n):
            a = a if obstacles[i] != 1 else sys.maxsize
            b = b if obstacles[i] != 2 else sys.maxsize
            c = c if obstacles[i] != 3 else sys.maxsize
            if obstacles[i] != 1:
                a = min(a, b + 1 if obstacles[i] != 2 else sys.maxsize, c + 1 if obstacles[i] != 3 else sys.maxsize)
            if obstacles[i] != 2:
                b = min(b, a + 1 if obstacles[i] != 1 else sys.maxsize, c + 1 if obstacles[i] != 3 else sys.maxsize)
            if obstacles[i] != 3:
                c = min(c, a + 1 if obstacles[i] != 1 else sys.maxsize, b + 1 if obstacles[i] != 2 else sys.maxsize)
        return min(a, b, c)