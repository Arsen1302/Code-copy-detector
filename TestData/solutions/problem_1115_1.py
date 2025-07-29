class Solution:
    def solution_1115_1(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        data = code + code
        result = [sum(data[i + 1: i + 1 + abs(k)]) for i in range(len(code))]
		# result = []
        # for i in range(len(code)):
        #     result.append(sum(data[i + 1: i + 1 + abs(k)]))
        if 0 > k:
            return result[k - 1:] + result[:k - 1]
        return result