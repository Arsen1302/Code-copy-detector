class Solution:
    def solution_749_5(self, label: int) -> List[int]:
        res = []
        bits = math.floor(math.log2(label)) + 1
        allOnes = (1 << bits)
        if not bits % 2:
            label = allOnes + (allOnes >> 1) - label - 1
        
        for i in range(bits, 0, -1):
            if i % 2:
                res.append(label)
            else:
                res.append(allOnes + (allOnes >> 1) - label - 1)
            allOnes >>= 1
            label >>= 1
        
        res.reverse()
        return res