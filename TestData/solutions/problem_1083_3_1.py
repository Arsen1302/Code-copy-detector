class Solution:
    
    def solution_1083_3_1(self, time):
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute
    
    def solution_1083_3_2(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        lookup = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            lookup[name].append(self.solution_1083_3_1(time))
        ans = []
        for name in sorted(lookup.keys()):
            times = lookup[name]
            times.sort()
            for i in range(1, len(times) - 1):
                if times[i + 1] - times[i - 1] <= 60:
                    ans.append(name)
                    break
        return ans