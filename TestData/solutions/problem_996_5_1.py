class Solution:
    def solution_996_5_1(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def solution_996_5_2(pluckDay):               # this function to check if a day is possible will be used in all the below solutions.
            flowers = bouquet = 0
            for d in bloomDay:
                if d > pluckDay: flowers = 0
                else:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
            return bouquet >= m
          
        arr = sorted(list(set(bloomDay)))
        
        for day in arr:
            if solution_996_5_2(day): return day
        return -1