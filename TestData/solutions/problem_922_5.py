class Solution:
    def solution_922_5(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat=0
        rs=defaultdict(set)
        for i,j in reservedSeats:
            rs[i].add(j)
        fr=n-len(rs)
        for i in rs.keys():
            fseat,lseat,mseat=1,1,1
            for j in range(2,6):
                if j in rs[i]:
                    fseat=0
                    break
            for k in range(9,5,-1):
                if k in rs[i]:
                    lseat=0
                    break
            if not fseat and not lseat:
                for l in range(4,8):
                    if l in rs[i]:
                        mseat=0
                        break
            else:
                mseat=0
            seat+=fseat+lseat+mseat
        return seat+(2*fr)