class Solution:
    def solution_1426_4(self, street: str) -> int:
        done = set()
        n = len(street)
        for i, c in enumerate(street):
            if c == 'H':
                if i - 1 in done or i + 1 in done:
                    continue
                if i + 1 <= n - 1:
                    if street[i + 1] == ".":
                        done.add(i + 1)
                        continue
                if i - 1 >= 0:
                    if street[i - 1] == ".":
                        done.add(i - 1)
                        continue
                return -1
        
        return len(done)