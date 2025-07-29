class Solution:
    def solution_586_5(self, digits: List[str], n: int) -> int:
        return sum((len(digits)**p) for p in range(1,len(str(n)))) + sum(sum(1 for digit in set(digits) if digit < d )*(len(digits)**(len(str(n))-i-1)) for i,(d,_) in enumerate(itertools.takewhile(lambda a:a[1] in set(digits) ,zip(str(n),digits[0]+str(n))))) + (1 if all(d in digits for d in str(n)) else 0)