class Solution:
    def solution_1570_2(self, bottom: int, top: int, special: List[int]) -> int:
        c = 0 
        special.sort()
        c = special[0]-bottom
        bottom = special[0]
        for i in range(1,len(special)):
            if special[i]-bottom>1:
                c = max(c,special[i]-bottom-1)
            bottom = special[i]
        if top-bottom>1:
                c = max(c,top-bottom)
        return c