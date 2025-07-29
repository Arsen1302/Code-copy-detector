class Solution:
    def solution_1657_2_1(self, mat: List[List[int]], cols: int) -> int:
        res = []
        M = len(mat)
        N = len(mat[0])
        def solution_1657_2_2(seen):
            count = 0
            for row in mat:
                flag = True
                for c in range(N): 
                    if row[c] == 1:
                        if c in seen:
                            continue
                        else:
                            flag = False
                            break
                if flag:    
                    count +=1   
            res.append(count)
                     
        def solution_1657_2_3(c,seen,cols):
            if cols == 0:
                solution_1657_2_2(seen)
                return
            if c == N:
                return
            else:
                seen.add(c)
                solution_1657_2_3(c+1,seen,cols-1)
                seen.remove(c)
                solution_1657_2_3(c+1,seen,cols)
        seen = set()
        solution_1657_2_3(0,seen,cols)
        return max(res)