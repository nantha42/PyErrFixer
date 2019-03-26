import os
class Process:
    def __init__(self,file):
        t = "import %s"%(file)
        noerror = False
        while not noerror:
            try:
                exec(t)
                print("noerror = True")
            except IndentationError as e:
                print("Indentation error")
                self.correctIdentation(file)
                noerror = True

    def correctIdentation(self,file):
        f = open(file+'.py','r')
        lines = f.read()
        correctedlines = []
        lines = lines.split('\n')
        lineno = 1
        for line in lines:
            level = self.countindentationlevel(line);
            print("indentation @ line=",lineno,"is ",level)
            #if level%4 != 0:
            lineno+=1
        print(lines)

    def countindentationlevel(self,line):
        count =0
        for i in line:
            if i == ' ':
                count+=1
            else:
                break
        return count
        pass

if __name__ ==  "__main__":
    p = Process("testfile")
