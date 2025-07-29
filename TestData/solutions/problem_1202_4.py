class Solution:
    def solution_1202_4(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            sumi = 0
            for j in range(len(boxes)):
                if(boxes[j] == '1'):
                    sumi += abs(j - i)
            arr.append(sumi)
        
        return arr