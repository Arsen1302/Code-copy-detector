class Solution:
    def solution_199_4(self, input: str) -> int:
        input = input.split('\n')
        path, ans, total = [], 0, 0
        for line in input:
            tabs = line.count('\t')
            while len(path) > tabs: total -= path.pop()
            path.append(len(line) - tabs)
            total += path[-1]
            if '.' in line: ans = max(ans, total + len(path) - 1)
        return ans