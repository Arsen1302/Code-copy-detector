class Solution:
    def solution_470_4(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx<sx or ty<sy:
            return False
        elif tx==sx:
            if (ty-sy)%sx==0:
                return True
            else:
                return False
        elif ty==sy:
            if  (tx-sx)%sy==0:
                return True
            else:
                return False
        else:
            return self.solution_470_4(sx,sy,tx-ty,ty) or self.solution_470_4(sx,sy,tx,ty-tx)