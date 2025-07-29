class Solution:
    def solution_430_3_1(self, source):
	    #decide the order for processing, return True if need to first process '//'
        def solution_430_3_2(line, commenting): 
            atype, btype, ctype = line.find('//'), line.find('/*'), line.find('*/')
            if atype != -1 and ctype != -1 and commenting:
                if commenting and ctype > atype: 
                    return False
                else: return ctype > atype
            elif atype != -1 and btype != -1:
                return btype > atype
            return atype != -1

        commenting, outputs, remained = False, [], ''
        for line in source:
            output = []
            while True: #only execute one time in most cases
			
			    #processing '//'
                if line.find('//') != -1 and solution_430_3_2(line, commenting):
                    line = line[:line.find('//')]
                    if len(line) > 0: output.append(line)
                
				#processing '/*'
                if not commenting and line.find('/*') != -1:
                    remained, line, commenting = line[:line.find('/*')], line[line.find('/*')+2:], True

				#processing '*/', call the main body again if there are some remainings comments in this line
                if commenting and line.find('*/') != -1:
                    line = line[line.find('*/')+2:]
                    line, remained, commenting =remained + line, '', False
                    #processing unfinished comments
                    if line.find('//')!=-1 or line.find('/*')!=-1 or line.find('*/')!=-1: continue
                    if len(line) > 0: output.append(line)
                break

            if len(output) > 0: outputs.append(''.join(output)) #lines with comments removed
            elif not commenting and len(line) > 0: outputs.append(line) #normal lines
        return outputs