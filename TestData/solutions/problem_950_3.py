class Solution:
    def solution_950_3(self, croakOfFrogs: str) -> int:
        """Reduction to interval overlap algorithm."""
        if not croakOfFrogs:
            return 0
        from collections import defaultdict
        positions = defaultdict(list)
        for i, c in enumerate(croakOfFrogs):
            positions[c].append(i)
        num_of_croaks = len(positions["c"])
        # check length
        for c in "croak":
            if num_of_croaks != len(positions[c]):
                return -1
        # check order to reduce to interval problem
        for i in range(num_of_croaks):
            if positions["c"][i] < positions["r"][i] < \
                    positions["o"][i] < positions["a"][i] < positions["k"][i]:
                continue
            else:
                return -1
        # interval overlap algorithm on c and k without overlap handling
        max_num = 1
        current_num = 1
        # first entry is always a c and irrelevant
        positions["c"].pop(0)
        while positions["c"]:
            # get next interval start
            current = positions["c"].pop(0)
            # check if it frees any frogs
            while current > positions["k"][0]:
                positions["k"].pop(0)
                current_num -= 1
            # account for new frog assignment to c
            current_num += 1
            max_num = max(max_num, current_num)
        return max(max_num, current_num)