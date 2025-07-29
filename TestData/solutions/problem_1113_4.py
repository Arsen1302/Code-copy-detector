class Solution:
    def solution_1113_4(self, s: str) -> int:
        deleted_elements = 0
        counter = Counter(s)
        freq_values = sorted(counter.values())[::-1]
        for index in range(len(freq_values)):
            while freq_values[index] != 0 and freq_values[index] in freq_values[:index] + freq_values[index+1:]:
                freq_values[index] -= 1
                deleted_elements += 1
        return deleted_elements