class Solution:
    def solution_741_4(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        used = defaultdict(lambda:0)
        ans = 0
        combined = sorted([(values[i],labels[i]) for i in range(n)],reverse = True)
        for value,label in combined:
            if numWanted == 0: break
            if used[label] < useLimit:
                used[label] += 1
                ans += value
                numWanted -= 1
        return ans