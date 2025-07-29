class Solution:
    
    def solution_901_2_1(self,year):
        
        return not(year % 400) or year % 100 and not(year % 4) # Leap year Condition
    
    def solution_901_2_2(self,year):
        
        year_days = 0
        
        for i in range(1971,year): # We need some reference 1971 is reference here lowest possible year in constairnts. You can take anything which will be lesser than given two dates.
            
            # To find distance between a and b. We are taking some reference which is smaller than both a and b. like if we need to find 100 - 200 we can take 0 as reference and find  0 - 100 and 0- 200 then find 100 - 200 which is -100 easily.
            
            # Directly if we try to find a - b many conditions will be there and it will end up having an headache
            
            if self.solution_901_2_1(i):
                
                year_days += 366
                
            else:
                
                year_days +=  365
        
        return year_days
    
    def solution_901_2_3(self,m,year):
        
        month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        month_days = 0
        
        for i in range(1,m):
            
            if i==2: # i is number of month like 1 for Jan and 2 for feb
                
                # for leap year feb will have 29 days i.e. x will be 1
                
                month_days += month[i] + int(self.solution_901_2_1(year))
                
            else:
                
                month_days += month[i]
        
        return month_days
        
        
    def solution_901_2_4(self, date1: str, date2: str) -> int:
        
        
        year1,month1,date1 = map(int,date1.split("-"))
        
        year2,month2,date2 = map(int,date2.split("-"))
        
        return abs ((self.solution_901_2_2(year1) + self.solution_901_2_3(month1,year1) + date1) - (self.solution_901_2_2(year2) + self.solution_901_2_3(month2,year2) + date2))