class Solution:
    def solution_741_2(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans = 0 
        freq = defaultdict(int)
        for value, label in sorted(zip(values, labels), reverse=True): 
            if 0 < num_wanted and freq[label] < use_limit: 
                ans += value
                num_wanted -= 1
                freq[label] += 1
        return ans