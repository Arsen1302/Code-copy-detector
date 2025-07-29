class Solution:
    def solution_1061_4(self, mat: List[List[int]]) -> int:
        ans = []
        count = 0
        rightcount = len(mat[0]) - 1
        for i in range(len(mat)):
            if rightcount == count: ans.append(mat[i][count])
            if i == count and rightcount != count:
                ans.append(mat[i][count])
                ans.append(mat[i][rightcount])
            count += 1
            rightcount -= 1
        return sum(ans)