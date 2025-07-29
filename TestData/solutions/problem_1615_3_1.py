class Solution:
    def solution_1615_3_1(self, start: str, target: str) -> bool:

        i = self.solution_1615_3_2(0, start)  ## starting position of the valid chacters in "Start"
        j = self.solution_1615_3_2(0, target)  ## starting position of the valid characters in "target"

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0:
            return False

        while True:
            if start[i]!=target[j]: return False ## if they dont match return False
            if start[i]=='R' and i > j: return False ## since we are at 'R", we can only move right. if i >j then there is no way we can get the result. Example. Start : _R  Target=R_  in this case i=1 > j=0 
            if start[i] == 'L' and i < j: return False ## since we are at "L", we can only move left. if i<j  then ther eis no way we can get the result. Example Start : L_ Target =_L . in this case i=0 < j=1

            i = self.solution_1615_3_2(i+1,start) ## check for the next character ('R' or 'L') in the starting string string
            j = self.solution_1615_3_2(j + 1, target) ## check for the next character ('R' or 'L') in the Target string

            if i < 0 and j < 0: ## if both i and j are negative then we have explored all characters
                return True
            if i < 0 or j < 0: ## if this happens then return False.
                return False

    def solution_1615_3_2(self, startingPosition, String):

        i = startingPosition 
        while i < len(String) and String[i] == '_':
            i += 1
        if i == len(String):
            return -1

        return i