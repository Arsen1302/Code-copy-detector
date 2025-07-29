class Solution:
    def solution_438_5(self, asteroids: List[int]) -> List[int]:
        INITIAL, PROCESS = 0, 1
        state = INITIAL
        s1, s2 = asteroids, []

        while True:
            if state == INITIAL:
                s2.append(s1.pop())
                state = PROCESS
            elif state == PROCESS:
                a, b = s1.pop(), s2.pop()
                if (a > 0 and b < 0) and a + b == 0: pass #Wrong directions and equal magnitude 
                elif (a < 0 and b > 0) or a * b > 0:      #Same sign or right direction
                    s2.append(b)
                    s2.append(a)
                elif a * b < 0: #Diff sign
                    if abs(a) > abs(b): s1.append(a) 
                    else: s2.append(b)

            if not s1: break
            if not s2: state = INITIAL

        return reversed(s2)