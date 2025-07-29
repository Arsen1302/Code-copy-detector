class Solution:
    def solution_208_5(self, n: int) -> int:
        ans = 0
        groups = [[k, len(list(g))] for k, g in itertools.groupby(map(int, bin(n)[2:]))]
        for i in range(len(groups)-1, 0, -1):
            k, glen = groups[i]
            if not glen:
                continue
            if not k:
                ans += glen
            elif glen == 1:
                ans += 2
            else:
                if groups[i-1][1] == 1:
                    ans += glen + 1
                    groups[i-1][1] = 0
                    groups[i-2][1] += 1
                else:
                    ans += glen + 2
        if groups[0][1] == 1:
            return ans
        return ans + groups[0][1] + int(groups[0][1] > 2)