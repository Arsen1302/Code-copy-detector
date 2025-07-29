class Solution:
    def solution_1433_3(self, digits: List[int]) -> List[int]:
        digits = Counter(digits)
        result = []
        for d1 in range(1, 10):
            for d2 in range(10):              
                for d3 in range(0, 10, 2):               
                    if not Counter([d1, d2, d3]) - digits:
                        result.append(100 * d1 + 10 * d2 + d3)
                    
        return result