class Solution:
    def solution_547_3(self, bills: List[int]) -> bool:
        d = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                d[5] += 1
            if bills[i] == 10:
                if d[5] >= 1:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return False
            if bills[i] == 20:
                if (d[5] >= 1 and d[10] >= 1):
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True