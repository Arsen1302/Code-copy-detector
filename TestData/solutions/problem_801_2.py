class Solution:
def solution_801_2(self, position: List[int]) -> int:
    
    dic = defaultdict(int)
    for n in position:
        dic[n%2] += 1
        
    return min(dic[0],dic[1])