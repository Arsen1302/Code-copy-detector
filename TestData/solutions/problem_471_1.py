class Solution:
    def solution_471_1(self, answers: List[int]) -> int:
        return sum((key+1) * math.ceil(freq / (key+1)) if key+1 < freq else key+1 for key, freq in collections.Counter(answers).items())