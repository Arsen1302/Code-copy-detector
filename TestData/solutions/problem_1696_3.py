class Solution:
    def solution_1696_3(self, num: int) -> bool:
        if num <= 18:
		   #Adding 1 digit number, a, and its reverse, also a: 2a
            if num % 2 == 0:
                return True
			#Adding 2 digit number, 10a+b, and its reverse, 10b+a: 11a+11b
            if num % 11 == 0:
                return True
            return False
        elif num <= 198:
            if num % 11 == 0:
                return True
			#Adding 3 digit number, 100a+10b+c, and its reverse, 100c+10b+a: 101a+20b+101c
            for b in range(10):
                newNum = (num - 20 * b)
				# checking last condition since a+c can be up to 18
                if newNum > 0 and newNum % 101 == 0 and newNum // 101 != 19: 
                    return True
            return False
        # rest follows similar pattern
        elif num <= 1998:
            for b in range(10):
                newNum = (num - 20 * b)
                if newNum > 0 and newNum % 101 == 0 and newNum // 101 != 19:
                    return True
            for bc in range(19):
                newNum = (num - 110 * bc)
                if newNum > 0 and newNum % 1001 == 0 and newNum // 1001 != 19:
                    return True  
            return False
        elif num <= 19998:
            for c in range(10):
                for bd in range(19):
                    newNum = (num - 200 *c - 1010 * bd)
                    if newNum > 0 and newNum % 10001 == 0 and newNum // 10001 != 19:
                        return True  
            for bc in range(19):
                newNum = (num - 110 * bc)
                if newNum > 0 and newNum % 1001 == 0 and newNum // 1001 != 19:
                    return True  
            return False
        elif num <= 199998: # 10**5 - 2
            for c in range(10):
                for bd in range(19):
                    newNum = (num - 200 *c - 1010 * bd)
                    if newNum > 0 and newNum % 10001 == 0 and newNum // 10001 != 19:
                        return True  
            for cd in range(19):
                for be in range(19):
                    newNum = (num - 100100 *cd - 100010 * be)
                    if newNum > 0 and newNum % 100001 == 0 and newNum // 100001 != 19:
                        return True  
            return False