class Solution:
    def solution_134_4_1(self, num: int) -> str:
        if not num: return 'Zero'
        ones = {1:' One', 2:' Two', 3:' Three', 4:' Four', 5:' Five', 6:' Six', 7:' Seven', 8:' Eight', 9:' Nine', 
				10:' Ten', 11:' Eleven', 12:' Twelve', 13:' Thirteen', 14:' Fourteen', 15:' Fifteen', 16:' Sixteen', 
				17:' Seventeen', 18:' Eighteen', 19:' Nineteen'}
        tens = {2:' Twenty', 3:' Thirty', 4:' Forty', 5:' Fifty', 6:' Sixty', 7:' Seventy', 8:' Eighty', 9:' Ninety'}
		
        self.output = ''
        def solution_134_4_2(num):
            if num // 1000000000:
                solution_134_4_2(num // 1000000000)
                self.output += ' Billion'
                solution_134_4_2(num % 1000000000)
            elif num // 1000000:
                solution_134_4_2(num // 1000000)
                self.output += ' Million'
                solution_134_4_2(num % 1000000)
            elif num // 1000:
                solution_134_4_2(num // 1000)
                self.output += ' Thousand'
                solution_134_4_2(num % 1000)
            elif num // 100:
                solution_134_4_2(num // 100)
                self.output += ' Hundred'
                solution_134_4_2(num % 100)
            elif num // 10 - 1 > 0:
                self.output += tens[num // 10]
                solution_134_4_2(num % 10)
            elif num:
                self.output += ones[num]
        solution_134_4_2(num)
        return self.output[1:]