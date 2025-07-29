class Solution:
    def solution_470_3(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if tx == sx:
                return (ty - sy) % sx == 0
            elif ty == sy:
                return (tx - sx) % sy == 0
            elif tx > ty:
                tx %= ty
            else:
                ty %= tx
        return False