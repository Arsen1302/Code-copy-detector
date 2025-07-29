class Solution:
    def solution_1440_4(self, rings: str) -> int:
        count = 0
        dic = collections.defaultdict(set)
        for i in range(1,len(rings),2):
            dic[rings[i]].add(rings[i-1])
        for k,v in dic.items():
            if len(v) == 3:
                count += 1
        return count