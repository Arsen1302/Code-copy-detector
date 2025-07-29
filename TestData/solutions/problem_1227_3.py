class Solution:
    def solution_1227_3(self, word: str) -> int:
        out = ''
		
        #Replace every non digits by spaces
        for char in word: 
            if char.isdigit():
                out = out + char
            
            else:
                out = out + ' '
        
		#Cleaning up None characters (double spaces) and converting digits from str to int
        out = out.split(' ')
        out_ = []
        
        for number in out: 
            if number != '':
                out_.append(int(number))
        
		#Using set() for filtering out repeat numbers
        return len(set(out_))