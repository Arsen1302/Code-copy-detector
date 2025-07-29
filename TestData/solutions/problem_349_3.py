class Solution:
    def solution_349_3(self, expression: str) -> str:
        # get all the fractions separately: e.g: "-1/2+1/2" -> ['-1/2', '1/2']
        fractions = re.findall(r'-*\d+/\d+', expression)
        
        # separate the numerators and denominators-> ['-1/2', '1/2'] -> [-1, 1] , [2, 2]
        numerators, denominators = [], []
        for fraction in fractions:
            n, d = map(int, fraction.split('/'))
            numerators.append(n)
            denominators.append(d)
        
        # find the lcm of the denominators
        lcm = reduce(math.lcm, denominators)
        # find with what number the denominators and numerators are to be multipled with
        multiples = [lcm // d for d in denominators]
        # multiply the multipler for each of the numerator
        numerators = [n*m for n, m in zip(numerators, multiples)]
        # multiply the multipler for each of the denominator
        denominators = [d*m for d, m in zip(denominators, multiples)]
        
        # now the denominators are all equal; so take just one; and add the numerator
        numerator, denominator = sum(numerators), denominators[0]
        # find if the numerator and denomitors can further of be reduced...
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        return f'{numerator}/{denominator}'