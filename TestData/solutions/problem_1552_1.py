class Solution:
    def solution_1552_1(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end, res = [], [], []
        for i in flowers:
            start.append(i[0])
            end.append(i[1])
        start.sort() #bisect only works with sorted data
        end.sort()

        for p in persons:
            num = bisect_right(start, p) - bisect_left(end, p)
            res.append(num)
        return res
#bisect_right(start, p) gives you the number of flowers that are in full bloom at person p.
#bisect_left(end, p) gives you number of flowers that are not in full bloom at person p.
#we have to tighten our bound to get exact number of flowers that are in bloom or not, thats why we are using right and left of bisect module.