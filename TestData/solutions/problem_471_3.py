class Solution:
    def solution_471_3(self, answers: List[int]) -> int:
        freqs = Counter(answers)

        total = 0
        for ans, freq in freqs.items():
            total += (ceil(freq / (ans + 1)))*(ans + 1)

        return total