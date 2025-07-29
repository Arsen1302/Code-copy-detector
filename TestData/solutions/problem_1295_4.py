class Solution:
    def solution_1295_4(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        a = b = c = 0
        for i in triplets:
            if i[0] == target[0] and i[1] <= target[1] and i[2] <= target[2] or i[1] == target[1] and i[0] <= target[0] and i[2] <= target[2] or i[2] == target[2] and i[1] <= target[1] and i[0] <= target[0]:
                a = max(a,i[0])
                b = max(b,i[1])
                c = max(c,i[2])
        return True if [a,b,c] == target else False