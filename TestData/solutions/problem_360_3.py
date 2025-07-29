class Solution:
    def solution_360_3(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        counter = collections.Counter(tasks)
        maxCount = 0
        maxValue = max(counter.values())
        for cha, val in counter.items():
            if val == maxValue:
                maxCount += 1
        return max((n + 1) * (maxValue - 1) + maxCount ,len(tasks))