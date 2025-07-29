class Solution:
    def solution_1425_4_1(self, words1: List[str], words2: List[str]) -> int:
                       
        counter = 0
        
        count_words_1 = solution_1425_4_2(words1)
                
        count_words_2 = solution_1425_4_2(words2)    
            
        count_words_1 = solution_1425_4_3(count_words_1)
                
        count_words_2 = solution_1425_4_3(count_words_2)   
        
        # Check if two dictionarys have same keys and if so, counts them.
        
        for i in count_words_2.keys():
            
            if i in count_words_1:
                
                counter += 1                
                               
        return counter
        
 # Helper function that will solution_1425_4_2 a list into a dictionary.
 # List elements represented as KEYS and list element's occurence represented as VALUES.
    
def solution_1425_4_2(array: List[str]):
    
    d = dict()
    
    for i in array:
        
        if i in d:
            
            d[i] += 1
            
        else:
            
            d[i] = 1
            
    return d         

# Helper method that search and deletes keys that have a value that is not 1.

def solution_1425_4_3(dict):
    
    for key in list(dict.keys()):
        
        if dict[key] != 1:
            
            del dict[key]
            
    return dict    
	
 # If you like my work, then I'll appreciate your like. Thanks.
	```