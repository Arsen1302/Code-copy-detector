class Solution:
    def solution_1401_2_1(self, parents: List[int]) -> int:
        tree = [[] for _ in parents]
        for i, x in enumerate(parents): 
            if x >= 0: tree[x].append(i)
                
        freq = defaultdict(int)
        
        def solution_1401_2_2(x): 
            """Return count of tree nodes."""
            left = right = 0
            if tree[x]: left = solution_1401_2_2(tree[x][0])
            if len(tree[x]) > 1: right = solution_1401_2_2(tree[x][1])
            score = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1)
            freq[score] += 1
            return 1 + left + right
        
        solution_1401_2_2(0)
        return freq[max(freq)]