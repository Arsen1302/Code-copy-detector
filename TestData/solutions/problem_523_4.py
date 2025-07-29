class Solution:
    def solution_523_4(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        max_p = 0
        n = len(img1)

        for r in range(n, 0, - 1):
            for d in range(n, 0, - 1):
                if max_p >= r * d:
                    break
                t1, t2, t3, t4 = 0, 0, 0, 0
                moved_r, moved_d = n - r, n - d

                for i in range(moved_r, n):
                    for j in range(moved_d, n):
                        if img1[i - moved_r][j - moved_d] == img2[i][j] == 1:
                            t1 += 1
                        if img1[i - moved_r][j] == img2[i][j - moved_d] == 1:
                            t2 += 1
                        if img1[i][j - moved_d] == img2[i - moved_r][j] == 1:
                            t3 += 1
                        if img2[i - moved_r][j - moved_d] == img1[i][j] == 1:
                            t4 += 1
                
                max_p = max(max_p, t1, t2, t3, t4)
        
        return max_p