class Solution:
    def solution_165_2(self, preorder: str) -> bool:
        outlet = 1
        for x in preorder.split(","): 
            if outlet == 0: return False #intermediate 
            outlet += 1 if x != "#" else -1
        return outlet == 0  #end result