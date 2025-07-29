class Solution:
    def solution_896_5(self, events: List[List[int]]) -> int:
        events.sort(key=lambda event: event[1])
        bitmask = 0
        for start, end in events:
            mask = ((1 << (end + 1)) - 1) ^ ((1 << start) - 1)
            if cover := (~bitmask &amp; mask):
                bitmask |= cover &amp; (-cover)
        return f'{bitmask:b}'.count('1')