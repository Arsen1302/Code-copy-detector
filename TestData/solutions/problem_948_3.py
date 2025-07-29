class Solution:
    def solution_948_3(self, s: str) -> str:
        
        numbers = [c for c in s if c.isdigit()]
        letters = [c for c in s if c.isalpha()]
        diff = abs(len(numbers) - len(letters))
        
        if diff > 1:
            return ''
        if diff == 0:
            return ''.join([item for pair in zip(numbers, letters) for item in pair])
        
        longer  = numbers if len(numbers) > len(letters) else letters
        shorter = numbers if len(numbers) < len(letters) else letters
        
        return ''.join([item for pair in zip(longer, shorter) for item in pair] + [longer[-1]])