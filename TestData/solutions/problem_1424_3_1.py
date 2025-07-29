class Solution:
    def solution_1424_3_1(self, k: int, n: int) -> int:
        def solution_1424_3_2(uptonow: str, remaining_count: int):
            '''Generator for yielding next base k symmetric string'''
            if not uptonow:
                yield from itertools.chain.from_iterable(solution_1424_3_2(str(i), remaining_count - 1) for i in range(1, k))
            elif not remaining_count:
                yield uptonow
            elif remaining_count > len(uptonow):
                yield from itertools.chain.from_iterable(
                    solution_1424_3_2(uptonow + str(i), remaining_count - 1) for i in range(k))
            else:
                yield from solution_1424_3_2(uptonow + uptonow[remaining_count - 1], remaining_count - 1)

        def solution_1424_3_3():
            '''Generating Symmetric base k string with different lengths'''
            number_length = 1
            while True:
                yield from solution_1424_3_2(remaining_count=number_length, uptonow='')
                number_length += 1

        res = 0
        base_k_symmetric_generator = solution_1424_3_3()
        for _ in range(n):
            while True:
                next_symmetric_base_k = next(base_k_symmetric_generator)
                base10 = int(next_symmetric_base_k, k)
                base10_string = str(base10)
                if base10_string == base10_string[::-1]:
                    break
            res += base10

        return res