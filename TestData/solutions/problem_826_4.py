class Solution:
    def solution_826_4(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for x in range(k):
            lst=collections.deque()
            for i in range(len(grid)):
                grid[i]=collections.deque(grid[i])
                grid[i].rotate(1)
                # print(i)
                lst.append(grid[i][0])
            # print(grid)
            lst.rotate(1)
            for i in grid:
                a=lst.popleft()
                i[0]=a
        return grid