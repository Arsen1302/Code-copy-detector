class Solution:
    def solution_350_5(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points, dic = [p1, p2, p3, p4], {}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dic[dis] = dic.get(dis:=(points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2, 0) + 1
        return len(ret:=sorted(dic.keys())) == 2 and dic[ret[0]] == 4 and ret[0] * 2 == ret[1]