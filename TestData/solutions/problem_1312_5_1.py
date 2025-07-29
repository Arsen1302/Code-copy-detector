class Solution:
    def solution_1312_5_1(self, target, n):
        i, j = 1,n
        while i <= j:
            mid = (i+j)//2
            s = mid*mid
            # print(i,j, mid, s)
            if s  == target:
                return True
            elif s < target:
                i = mid + 1
            else:
                j = mid - 1
        return False
    def solution_1312_5_2(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                cond = self.solution_1312_5_1(i*i + j*j, n)
                if cond:
                    ans += 1
                    # print(i,j)
        return ans