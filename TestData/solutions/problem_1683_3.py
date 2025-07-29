class Solution:
    def solution_1683_3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                vsum = 0
                for k in range(3):
                    for t in range(3):
                        # print(grid[i+k][j+t], end = " ")
                        if k==0 or k==2 or (k==1 and t==1):
                            vsum = vsum + grid[i+k][j+t]
                    # print()
                ans = max(ans, vsum)
                # print("--")
        # print("=" * 20)
        return ans