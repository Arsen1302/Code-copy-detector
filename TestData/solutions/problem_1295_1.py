class Solution:
    def solution_1295_1(self, triplets: List[List[int]], target: List[int]) -> bool:
        i = 1
        cur = []
        for a,b,c in triplets:
            if a<=target[0] and b<=target[1] and c<= target[2]:
                cur = [a,b,c]
                break
        if not cur:
            return False
        while i<len(triplets):
            if cur == target:
                return True
            a,b,c = triplets[i]
            x,y,z = cur
            if max(a,x)<=target[0] and max(b,y)<=target[1] and max(c,z)<=target[2]:
                cur = [max(a,x), max(b,y), max(c,z)]
               
            
            i+= 1
        if cur == target:
            return True
        return False