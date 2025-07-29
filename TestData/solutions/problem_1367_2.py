class Solution:
    def solution_1367_2(self, rectangles: List[List[int]]) -> int:
        count=0
        d=dict()
        for i in range(len(rectangles)):
            ratio=rectangles[i][0]/rectangles[i][1]
            if ratio not in d:
                d[ratio]=1
            else:
                count+=d[ratio]
                d[ratio]+=1
        return count