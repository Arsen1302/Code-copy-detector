class Solution:
    def solution_741_5(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(((value, label) for value, label in zip(values, labels)), reverse=True)
        score = 0
        uses = collections.Counter()
        
        for value, label in items:
            if uses[label] == useLimit:
                continue
            score += value
            if numWanted == 1:
                break
            uses[label] += 1
            numWanted -= 1       
        
        return score