class Solution:
    def solution_1145_3(self, number: str) -> str:
        res = ""
        
        # step 1: removing all non number characters
        number = re.sub('[^0-9]','',number)
        
        # step 2: grouping the digits from left to right until there are 4 or fewer digits
        while len(number) > 4:
            res += number[:3] + '-'
            number = number[3:]
        
        # step 3: 3 digits and 2 digits logic is the same
        if len(number) == 4:
            res += number[:2] + '-' + number[2:]
        else:
            res += number
            
        return res