class Solution:
    def solution_1202_5(self, boxes: str) -> List[int]:
        n = len(boxes)
        dpleft, dpright = [0]*n, [0]*n
        countleft, countright = int(boxes[0]), int(boxes[-1])
        ans = [0]*n
        
        for i in range(1, n):
            dpleft[i] = dpleft[i-1] + countleft
            if boxes[i] == '1':
                countleft += 1
        
        for i in range(n-2, -1, -1):
            dpright[i] = dpright[i+1] + countright
            if boxes[i] == '1':
                countright += 1
        
        for i in range(len(boxes)):
            ans[i] = dpleft[i]+dpright[i]
        
        return ans