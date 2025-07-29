class Solution:
    def solution_492_5(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s =set()
        for word in words:
            string = ""
            for ele in word:
                string+=arr[ord(ele)-97]
            s.add(string)
        return len(s)