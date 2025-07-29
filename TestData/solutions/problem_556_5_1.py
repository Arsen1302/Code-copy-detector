class Solution:
    def solution_556_5_1(self,num):
        char_arr = str(num)
        table = dict()
        for char in char_arr:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        return table
            
            
    def solution_556_5_2(self, N: int) -> bool:
        num_tab = self.solution_556_5_1(N)
        i = 0
        while i < 64:
            if num_tab == self.solution_556_5_1(pow(2,i)):
                return True
            else:
                i += 1
        return False