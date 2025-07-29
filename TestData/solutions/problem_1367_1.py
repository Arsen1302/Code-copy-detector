class Solution:
    def solution_1367_1(self, rectangles: List[List[int]]) -> int:
        preSum = []
        for rec in rectangles:
            preSum.append(rec[1]/rec[0])
        
        dic1 = {}
        for i in range(len(preSum)-1, -1, -1):
            if preSum[i] not in dic1.keys():
                dic1[preSum[i]] = [0,1]
            else:
                dic1[preSum[i]][0] = dic1[preSum[i]][0] + dic1[preSum[i]][1]
                dic1[preSum[i]][1] += 1
        
        return sum ([v[0] for v in dic1.values()])