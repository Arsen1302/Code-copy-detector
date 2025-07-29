class Solution:
    def solution_1495_3(self, num: int) -> List[int]:
        if num%3==0:
            c=num//3
            return [c-1,c,c+1] 
        else:
            return []