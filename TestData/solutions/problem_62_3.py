class Solution:
    def solution_62_3(self, points: List[List[int]]) -> int:
        d1,out={},[1]
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1,y1,x2,y2 = points[i][0],points[i][1],points[j][0],points[j][1]
                if x2-x1!=0: slope,intercept = (y2-y1)/(x2-x1),(y1*x2-x1*y2)/(x2-x1)
                else: slope,intercept = 'inf',(y1*x2-x1*y2)/(y1-y2)
                key = str(slope)+str(intercept)
                if key not in d1: d1[key]=[[x1,y1],[x2,y2]]
                else:
                    if [x1,y1] not in d1[key]: d1[key].append([x1,y1])
                    if [x2,y2] not in d1[key]: d1[key].append([x2,y2])                   
        for x in d1.values(): out.append(len(x))
        return max(out)