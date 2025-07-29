class Solution:
    def solution_470_5(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        q = [(sx, sy)]
        visit = set()
        visit.add((sx, sy))
        
        while q:
            num = len(q)
            for i in range(num):
                x, y = q.pop(0)
                if x == tx and y == ty:
                    return True
                if x <= tx and y <= ty:
                    if (x, x+y) not in visit:
                        visit.add((x, x+y))
                        q.append((x, x+y))
                    if (x+y, y) not in visit:
                        visit.add((x+y, y))
                        q.append((x+y, y))
        
        return False