class Solution:
    def solution_904_4(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        category = dict()
        for d in digits: category.setdefault(d%3, []).append(d)
        
        parity = sum(digits) % 3
        if parity != 0: 
            if len(category.get(parity, [])) > 0: 
                digits.remove(category[parity][-1])
            elif len(category.get(3-parity, [])) > 1: 
                digits.remove(category[3-parity][-1])
                digits.remove(category[3-parity][-2])
            else: 
                return ""
        
        return "0" if digits and not digits[0] else "".join(str(d) for d in digits)