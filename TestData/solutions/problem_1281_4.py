class Solution:
    def solution_1281_4(self, n: str, x: int) -> str:
        # if positive, insert when x > leading digit 
        # --> ensure we can obtain benefit from the leftmost (indicates largest improvement)
        # if negative, .. < leading digit
        # --> similar logic 
        
		# special case: 0
        if n == '0':
            return str(x)
        
        # positive
        if n[0] != '-':
            for i in range(len(n)):
                if x > int(n[i]):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        # negative 
        else:
            for i in range(1, len(n)):
                if x < int(n[i]):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)