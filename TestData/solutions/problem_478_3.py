class Solution:
    def solution_478_3(self, N: int) -> int:
        quantity = 0
        for num in range(1, N+1):
            tally = str(num)
            if any([True if x in '347' else False for x in tally]):
                continue
            if all([True if x in '018' else False for x in tally]):
                continue
            quantity += 1
        return quantity