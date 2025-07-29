class Solution:
    def solution_1401_3_1(self, parents: List[int]) -> int:
        tree = [[] for _ in parents]
        for i, x in enumerate(parents): 
            if x >= 0: tree[x].append(i)
        
        def solution_1401_3_2(x): 
            """Return count of tree nodes."""
            count = score = 1
            for xx in tree[x]: 
                cc = solution_1401_3_2(xx)
                count += cc
                score *= cc
            score *= len(parents) - count or 1
            freq[score] += 1
            return count
        
        freq = defaultdict(int)
        solution_1401_3_2(0)
        return freq[max(freq)]