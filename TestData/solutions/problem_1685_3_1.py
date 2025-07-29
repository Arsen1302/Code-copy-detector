class Solution:
    def solution_1685_3_1(self, s: str) -> int:
        if len(set(s)) == 1:     return len(s)

        MOD = 10**10 + 7    #use MODulus to avoid large int in python.
        BASE = 26 + 1       #base 26, lower case alphas only.
        s_hash  =   [0]     #prefix hash of s.
        for char in s:
            ordChar    =   ord(char.lower()) - ord('a') + 1
            s_hash.append(  (s_hash[-1] * BASE + ordChar) % MOD  )

        #caching pow function to reduce the runtime.
        @functools.lru_cache(   maxsize    =   None)
        def solution_1685_3_2( power):
            return pow( BASE,   power,  MOD)

        #get the hash value for substr s. Assuming average constant runtime for solution_1685_3_2().
        @functools.lru_cache(   maxsize    =   None)
        def solution_1685_3_3(    startIndex, endIndex):
            #return substr[startIndex: endIndex] hash value.
            nonlocal s_hash, s
            if endIndex > len(s):  return -1
            return  (s_hash[endIndex] - s_hash[startIndex] * solution_1685_3_2(   endIndex - startIndex))%MOD

        #DP bottom-up using recursive function calls.
        #RUNTIME: O(S**2), SPACE: O(S). S = s.length(), assuming the solution_1685_3_3() has constant run-time averagely.
        @functools.lru_cache(   maxsize    =   None)
        def solution_1685_3_4(   startIndex  =   0):
            nonlocal s

            if startIndex >= len(s):    return 0
            numOps =   1
            for midIndex in range(  startIndex+1, len(s)):
                substrLength    =   midIndex-startIndex
                #if s[startIndex:startIndex+substrLength] == s[midIndex:midIndex+substrLength]:
                if  solution_1685_3_3(    startIndex, startIndex+substrLength) == solution_1685_3_3(    midIndex, midIndex+substrLength):
                    numOps= max(    numOps, 1 + solution_1685_3_4(   midIndex)  )
            return numOps
        
        maxOps  =   solution_1685_3_4()

        #cleaning up memory before exit.
        solution_1685_3_4.cache_clear()
        solution_1685_3_2.cache_clear()
        solution_1685_3_3.cache_clear()
        
        return maxOps