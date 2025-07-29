class Solution:
    def solution_671_5(self, startValue: int, target: int) -> int:

        step = 0
        while target != startValue:
            if target < startValue:
                step = step + (startValue - target)
                return step
            else:
                if target%2 == 0:
                    target = target//2
                    step += 1
                else:
                    target = target+1
                    step+=1
        return step