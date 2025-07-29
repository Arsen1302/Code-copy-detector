class Solution:
    def solution_597_3(self, deck: List[int]) -> bool:
        d=defaultdict(int)
        for i in deck:
            d[i]+=1 
        for k in d:
            gcd=d[k]
            break
        for k in d:
            gcd=math.gcd(gcd,d[k])
        return gcd!=1