class Solution:
    def solution_904_1_1(self, digits: List[int]) -> str:
        def solution_904_1_2(r: int) -> str:
            if r:
                for i in range(3):
                    idx = 3 * i + r
                    if counts[idx]:
                        counts[idx] -= 1
                        break
                else:
                    rest = 2
                    for j in range(3):
                        idx = 3 * j + (-r % 3)
                        while rest and counts[idx]:
                            counts[idx] -= 1
                            rest -= 1
                        if not rest: break
                    if rest: return ''
            if any(counts):
                result = ''
                for i in reversed(range(10)):
                    result += str(i) * counts[i]
                return str(int(result))
            return ''

        total, counts = 0, [0] * 10
        for digit in digits:
            counts[digit] += 1
            total += digit
        return solution_904_1_2(total % 3)