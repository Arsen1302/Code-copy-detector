class Solution:
#Time-Complexity: O((m ^ m) * n), since branching factor in worst case is m and worst case height is #m for rec. tree and for each rec. call, we call solution_1329_5_2, which takes linear time with respect
#to n number of questions!
#Space-Complexity:O(m + m + m) -> O(m) space taken up due to call stack max depth, the boolean flag array, as well as the current built up pairings array!
    def solution_1329_5_1(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        #first define solution_1329_5_3 function!
        def solution_1329_5_2(s, m):
            student_answers = students[s]
            mentor_answers = mentors[m]
            ans = 0
            for i in range(len(student_answers)):
                if(student_answers[i] == mentor_answers[i]):
                    ans += 1
            return ans
        #m = number of students and mentors!
        m = len(students)
        #intialize boolean flag array for indices from 0 to m-1!
        bool_arr = [0] * m
        
        #we can define main recursive solution_1329_5_3 function!
        #4 paramters:
        #1. student : student index we are on making decision for to which mentor to pair up with!
        #2.cur: 2d array pass by ref. which will be list of all pairings in form of 
        #[si, mi], where si index student paired up with mi mentor!
        #3. s-> sum of compatability scores of all pair elements that are in cur so far locally!
        #4. b-> boolean array which tells us which index pos mentor element is not paired yet
        #and is available for use!
        res = 0
        def solution_1329_5_3(student, cur, s, b):
            nonlocal res, m
            #base case: we formed m pairs!
            if(len(cur) == m):
                #update answer!
                res = max(res, s)
                return
            
            #otherwise, we need to pair up current student with all available mentors
            #simply check each and every mentor from index 0 to m-1!
            for i in range(0, m, 1):
                #check if this mentor is available!
                if(b[i] == 1):
                    continue
                
                #if mentor is available, simply pair up current student with ith mentor!
                cur.append([student, i])
                #also we need to get updated_compatibility score!
                updated_score = s + solution_1329_5_2(student, i)
                #also, set the flag on for ith mentor to not make available for use in furhter
                #recursive calls!
                b[i] = 1
                #now, recurse and pass cur and b by ref while making choice
                #for the next student +1 index student as well as with new updated_score
                #for all pairings in cur in rec. call!
                solution_1329_5_3(student + 1, cur, updated_score, b)
                #once rec. call finishes and returns, we need to update cur and b!
                cur.pop()
                b[i] = 0
                
        solution_1329_5_3(0, [], 0, bool_arr)
        return res