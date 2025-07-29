class Solution:
    def solution_1450_3(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1:
            return False
        #Two pass solution
        #Left to right, check if there are enough "(" (including the locked==0 ones, that can be changed as we wish) to match ")". 
        Number_of_open_brackets = 0
        Number_of_closing_brackets = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                Number_of_open_brackets += 1
            else:
                Number_of_closing_brackets += 1
            if Number_of_closing_brackets > Number_of_open_brackets:
                return False
        #Right to Left, check if there are enough ")" (including the locked==0 ones, that can be changed as we wish) to match "(".  
        Number_of_open_brackets = 0
        Number_of_closing_brackets = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                Number_of_closing_brackets += 1
            else:
                Number_of_open_brackets += 1
            if Number_of_open_brackets > Number_of_closing_brackets:
                return False
        return True
#Need two pass because left to right one pass will not fix edge cases such as "))((", 0011. The two ( are apparently waiting to see if on the right side there is enough ) to match them