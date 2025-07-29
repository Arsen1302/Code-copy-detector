class Solution:
    def solution_562_5_1(self, piles: List[int], h: int) -> int:
        """
                            3 6 7 11   , h =8

                 speed = 1  3 6  7 11 =  28h > 8h
                 speed = 2  3 3  4 6  =  16h > 8h
                 speed = 3  1 2  3 4  =  10h > 8h
   minimum ----> speed = 4  1 2  2 3  =   8h = 8h <-------
                 speed = 5  1 2  2 3  =   8h = 8h
                 speed = 6  1 1  2 2  =   8h = 8h
                 speed = 7  1 1  1 2  =   5h < 8h
                 speed = 8  1 1  1 2  =   5h < 8h
                 speed = 9  1 1  1 2  =   5h < 8h
                 speed =10  1 1  1 2  =   5h < 8h
                 speed =11  1 1  1 1  =   4h < 8h
				 
				                           ^
                                           |
										we are searching the first 8 on this column.
        """
        self.piles = piles
        #print(self.piles)
        #ans1 = self.solution_562_5_2(h) # time limit exceeded
        ans2 = self.solution_562_5_3(h)
        return ans2
    
    def solution_562_5_2(self,h):
        l,r = 1,max(self.piles)
        for i in range(l,r+1):
            if self.solution_562_5_4(i) <= h:  
                return i
              
            
    def solution_562_5_3(self,h):
        l, r = 1, max(self.piles)
        while l < r:
            m = l + (r-l) // 2
            time = self.solution_562_5_4(m)
            if time > h:
                l = m + 1
            else:
                r = m
        return l
        
    def solution_562_5_4(self,k):  # return at current speed k, how much time needed to eat all the piles in the list
        time = 0
        for i in self.piles:
            curTime = ceil(i / k) 
            time += curTime
        return time