class Solution:
    def solution_1685_4_1(self, s: str) -> int:
        from collections import Counter
        N = len(s)
        global memo
        memo = {}
        #print('\n\nTest case -> s:', s, 'N:', N)
        return solution_1685_4_2(s)


def solution_1685_4_2(s):
    #print('Rem Start -> s:', s)
    global memo
    if s in memo:
        #print('MEMO found -> memo[s]:', memo[s])
        return memo[s]
    
    N = len(s)
    #print('N:', N)
    if N == 0:
        #print('Empty string case, s:', s)
        return 0
    
    if N == 1:
        # Remove entire string
        #print('Single char case, s:', s)
        memo[s] = 1
        return 1
    
    c = Counter(s)
    if c[s[0]] == N:
        # All chars are same
        memo[s] = N
        return N
    
    maxToRem = N // 2
    #print('maxToRem:', maxToRem)
    maxSteps = 1
    for numToRem in range(maxToRem, 0, -1):
        if s[:numToRem] == s[numToRem:2*numToRem]:
            #numCharsToRem,append(numToRem)
            #print('s:', s, 'numToRem:', numToRem, 'Removing', s[:numToRem])
            maxSteps = max(maxSteps, solution_1685_4_2(s[numToRem:])+1)
    
    memo[s] = maxSteps
    #print('s:', s, 'memo[s]:', memo[s])
    return maxSteps