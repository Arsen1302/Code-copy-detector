class Solution:
    def solution_861_5(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for i in arr:
            prefix_xor.append(prefix_xor[-1] ^ i)
        
        res = []
        for i, j in queries:
            res.append(prefix_xor[i] ^ prefix_xor[j+1])
        
        return res