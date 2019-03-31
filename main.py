import os
class Process:
    def __init__(self,file):

        self.readFile(file)

    def readFile(self,file1):
        f = open(file1, 'r')
        lines = f.read()
        lines = lines.split('\n')
        lineno = 1
        self.detect_indentation(lines)

    def detect_indentation(self,lines):
        indentstarted = False
        level = 0
        j=4
        correctedlines = []

        for i in lines:

            if '{' in i:
                s = ' ' * j * level
                correctedlines.append(s + i)
                level += 1


            elif '}' in i:
                level -= 1
                s = ' ' * j * level
                correctedlines.append(s+i)

            else:
                s = ' ' * j * level
                correctedlines.append(s + i)
            print(level,i)

        for i in correctedlines:
            print(i)


        pass

    def gcd(self,n,m):
        if m>0:
            return self.gcd(m,n%m)
        else:
            return n

    def count_indentation_level(self,line):
        count =0
        for i in line:
            if i == ' ':
                count+=1
            else:
                break
        return count
        pass

if __name__ ==  "__main__":
    p = Process("testfile.cpp")