class Solution:
    def solution_848_4(self, nums: List[int]) -> int:
        
        even_digit_width = lambda number: ( len( str(number) ) % 2 == 0 )
        return sum( map(even_digit_width, nums) , 0 )