class Solution:
    def solution_204_1_1(self, data: List[int]) -> bool:
        n = len(data)
        l = [2**i for i in range(7, -1, -1)]
        
        def solution_204_1_2(pos, X):
            f = data[pos]
            rem = data[pos+1:pos+X]
            ret = (f&amp;l[X]) == 0
            for i in range(X):
                ret &amp;= (f&amp;l[i]) != 0
            for num in rem:
                ret &amp;= (num&amp;l[0]) != 0
                ret &amp;= (num&amp;l[1]) == 0
            return ret
            
        @cache
        def solution_204_1_3(pos = 0):
            ret = False
            if pos == n:
                ret = True
            if pos + 3 < n:
                ret |= solution_204_1_2(pos, 4) and solution_204_1_3(pos + 4)
            if pos + 2 < n:
                ret |= solution_204_1_2(pos, 3) and solution_204_1_3(pos + 3)
            if pos + 1 < n:
                ret |= solution_204_1_2(pos, 2) and solution_204_1_3(pos + 2)
            if pos < n:
                ret |= solution_204_1_2(pos, 0) and solution_204_1_3(pos + 1)
            return ret
        
        return solution_204_1_3()