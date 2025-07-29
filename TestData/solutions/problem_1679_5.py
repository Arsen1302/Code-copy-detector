class Solution:
    def solution_1679_5(self, word: str) -> bool:
        counter = Counter(word)
        
        list = []
        for _, v in counter.items():
            if v:
                list.append(v)
        list.sort()
        
        if len(list) == 1: # example: 'ddddd'
            return True
        
        if list[-1] == 1: # example: 'abcdefg'
            return True
        
        if list[0] == 1 and list[1] == list[-1]: # example: 'bdddfff'
            return True
        
        if list[-1] == list[-2] + 1 and list[0] == list[-2]: # example: 'bbbdddgggg'
            return True
        
		# all other cases are bad conditions
        return False