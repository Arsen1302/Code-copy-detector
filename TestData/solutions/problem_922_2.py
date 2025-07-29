class Solution:
    def solution_922_2(self, n: int, reservedSeats: List[List[int]]) -> int:
        alloc = collections.defaultdict(set)
        ct = n*2
        while reservedSeats:
            x = reservedSeats.pop()
            if 1 < x[1] < 6:
                alloc[x[0]].add(1)
            elif 5 < x[1] < 10:
                alloc[x[0]].add(3)
            if 3 < x[1] < 8:
                alloc[x[0]].add(2)
        ct = 2*n
        for key, val in alloc.items():
            if val=={1,2,3}:
                ct-=2
            else:
                ct-=1
        return ct