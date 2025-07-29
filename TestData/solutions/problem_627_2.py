class Solution:
    def solution_627_2(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        ipush = 0
        ipop = 0
        
        try:
            while ipush < len(pushed) or ipop < len(popped):
                if len(s) == 0 or (len(s) != 0 and s[-1] != popped[ipop]):
                    s.append(pushed[ipush])
                    ipush += 1
                elif s[-1] == popped[ipop]:
                    s.pop()
                    ipop += 1
        except IndexError:
            return False
        
        return True