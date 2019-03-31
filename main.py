import os
import tkinter

class Process:
    def __init__(self,file=None):
        if file != None :
            self.readFile(file)

    def readFile(self,file1):
        f = open(file1, 'r')
        lines = f.read()
        lines = lines.split('\n')
        lineno = 1
        self.detect_indentation(lines)

    def isitindented(self,line,requiredspaces):
        actualspaces=0
        for i in line:
            if i == ' ':
                actualspaces += 1
            else:
                break

        if (requiredspaces - actualspaces) > 0:
            line = ' '*(requiredspaces-actualspaces) + line
        elif (requiredspaces - actualspaces) < 0:
            remo = (actualspaces - requiredspaces)
            while remo>0:
                line = line[1:]
                remo -=1

        return line

    def send_string(self,lines):
        lines = lines.split('\n')
        print(lines)
        correctedlines = self.detect_indentation(lines)
        file = ""
        for i in correctedlines:
            file += i+'\n'
        return file

    def detect_indentation(self,lines):
        indentstarted = False
        level = 0
        j=4
        correctedlines = []

        for i in lines:

            if '{' in i:

                s = ' ' * j * level
                correctedlines.append(self.isitindented(s+i,j*level))
                level += 1


            elif '}' in i:
                level -= 1
                s = ' ' * j * level
                correctedlines.append(self.isitindented(s+i,j*level))

            else:
                s = ' ' * j * level
                correctedlines.append(self.isitindented(s + i,j*level))


        #for i in correctedlines:
        #   print(i)
        return correctedlines
        pass

    def gcd(self,n,m):
        if m>0:
            return self.gcd(m,n % m)
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