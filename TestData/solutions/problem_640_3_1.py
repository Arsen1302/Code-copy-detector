class Solution:
    def solution_640_3_1(self, grid):
        return self.solution_640_3_2(grid)

    def solution_640_3_2(self, grid):
        '''                             |\0/|
        set area of cell like:          |3X1|
                                        |/2\|
        dye and count like flood fill
        '''
        N = len(grid)

        dye = [[[False] * 4 for _ in range(N)] for _ in range(N)]

        def solution_640_3_3(r, c, i):
            if not 0 <= r < N or not 0 <= c < N: return  # out of boundary
            if dye[r][c][i]: return  # already dyed

            if grid[r][c] == ' ':
                dye[r][c] = [True] * 4
                solution_640_3_3(r - 1, c, 2)  # ^
                solution_640_3_3(r + 1, c, 0)  # v
                solution_640_3_3(r, c - 1, 1)  # <
                solution_640_3_3(r, c + 1, 3)  # >
            elif grid[r][c] == '/':
                if i in [0, 3]:
                    dye[r][c][0] = True
                    dye[r][c][3] = True
                    solution_640_3_3(r - 1, c, 2)  # ^
                    solution_640_3_3(r, c - 1, 1)  # <
                else:
                    dye[r][c][1] = True
                    dye[r][c][2] = True
                    solution_640_3_3(r, c + 1, 3)  # >
                    solution_640_3_3(r + 1, c, 0)  # v
            else:  # \
                if i in [0, 1]:
                    dye[r][c][0] = True
                    dye[r][c][1] = True
                    solution_640_3_3(r - 1, c, 2)  # ^
                    solution_640_3_3(r, c + 1, 3)  # >
                else:
                    dye[r][c][2] = True
                    dye[r][c][3] = True
                    solution_640_3_3(r, c - 1, 1)  # <
                    solution_640_3_3(r + 1, c, 0)  # v

        count = 0

        for r in range(N):
            for c in range(N):
                for i in range(4):
                    # skip if already dyed
                    if dye[r][c][i]: continue
                    # count and dye solution_640_3_3
                    count += 1
                    solution_640_3_3(r, c, i)
        return count