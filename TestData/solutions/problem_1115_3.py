class Solution:
    def solution_1115_3(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        cracked = [] * len(code)
        if k < 0:
            for i in range(len(code)):
                total = 0
                for j in range(i - 1, i + k - 1, -1):
                    total += code[j % len(code)]
                cracked.append(total)
        else:
            for i in range(len(code)):
                total = 0
                for j in range(i + 1, i + k + 1):
                    total += code[j % len(code)]
                cracked.append(total)
        return cracked