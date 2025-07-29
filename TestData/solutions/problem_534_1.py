class Solution:
    def solution_534_1(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        while counter:
            n = groupSize
            start = min(counter.keys())
            while n:
                if start not in counter:
                    return False
                counter[start] -= 1
                if not counter[start]:
                    del counter[start]
                start += 1
                n -= 1
        return True