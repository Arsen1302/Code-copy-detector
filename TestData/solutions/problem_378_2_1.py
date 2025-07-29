class Solution:
    def solution_378_2_1(self, n: int) -> int:
        cache = {}
        def solution_378_2_2(screen, clipboard):
            if (screen, clipboard) in cache: return cache[(screen, clipboard)]
            if screen == n: return 0
            if screen > n: return float("Inf")
            
            copy_paste = solution_378_2_2(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = solution_378_2_2(screen + clipboard, clipboard) + 1

            cache[(screen, clipboard)] = min(copy_paste, paste)    
            return cache[(screen, clipboard)]
        
        return solution_378_2_2(1, 0)