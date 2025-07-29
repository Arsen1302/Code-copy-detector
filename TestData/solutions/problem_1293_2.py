class Solution:
    def solution_1293_2(self, words: List[str]) -> bool:
        
        joint = ''.join(words)
        set1 = set(joint)
        
        for i in set1 :
            if joint.count(i) % len(words) != 0 : return False 
        return True