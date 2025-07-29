class Solution:
    def solution_52_5_1(self, s: str, wordDict: List[str]) -> bool:
        memo = {}


        def solution_52_5_2(target, strings_bank, memo):    
            if target in memo:
                return memo[target]
            if target == "":
                return True
            for element in strings_bank: # for every element in our dict we check if we can start constructing the string "s"
                if element == target[0:len(element)]: # the remaining of the string "s" (which is the suffix) is the new target 
                    suffix = target[len(element):]
                    if solution_52_5_2(suffix, strings_bank, memo):
                        memo[target] = True
                        return True
            memo[target] = False
            return False


        return solution_52_5_2(s, wordDict, memo)