class Solution:
    def solution_73_3(self, numerator: int, denominator: int) -> str:
        
        # base case
        if numerator == 0:
            return '0'
        
        # result
        res = ''
        
        # positive and negative
        if (numerator > 0 and denominator < 0) or \
            (numerator < 0 and denominator > 0):
            res += '-'
        
        # absolute value
        numerator, denominator = abs(numerator), abs(denominator)
        
        # remainder as zero
        res += str(numerator//denominator)
        numerator %= denominator
        if numerator == 0:
            return res
        
        # add a dot .
        res += '.'
        
        # hashmap to write down the starting index of a repeated remainder
        hashmap = {}
        hashmap[numerator] = len(res)
        while numerator != 0:
            
            # continue to mutiply by 10
            numerator *= 10
            res += str(numerator//denominator)
            numerator %= denominator
            
            # check if it finds a repeated pattern
            if numerator in hashmap:
                index = hashmap[numerator]
                res = res[:index] + '(' + res[index:]
                res += ')'
                break
            else:
                hashmap[numerator] = len(res)
                 
        return res