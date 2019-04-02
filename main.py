import os
import tkinter


class Process:
    def __init__(self, file=None,path=""):
        self.windowlength = 3
        self.indentstarters = ['for ', 'if ', 'if(', 'else:', 'elif(', 'elif ', 'while ', 'while(', 'def ','with ','class ']
        self.indentenders = ['return ', 'pass']
        self.report = ""
        if file != None:
            other_than_indentederror = False
            error = True
            while (not other_than_indentederror) and error :
                try:
                    print("***************Starting to Execute**************")
                    command = "import %s" % (file)
                    #command1 = "python3 %s"
                    #os.system(command1)
                    exec(command)
                    print("*********program executed successfully**********")
                    error = False

                except IndentationError as ie:
                    print("***********Detected Indentation error********",ie)

                    self.addreport("Correcting Indentating error")
                    self.readFile(path+'/'+file+".py")

                except Exception:
                    self.addreport("Some other invalid syntax")
                    other_than_indentederror = True



    def addreport(self,report):
        self.report += report +'\n'

    def getreport(self):
        return self.report

    def printer(self,lines):
        for line in lines:
            self.addreport(line)

    def writeFile(self,lines,file1):
        str = self.listtostring(lines)
        f = open(file1,'w')
        f.write(str)
        f.close()


    def readFile(self, file1):
        f = open(file1, 'r')
        lines = f.read()
        lines = lines.split('\n')
        lineno = 1
        # self.detect_indentation(lines)

        lines = self.removeblanklines(lines)
        lines = self.firstline(lines)
        for i in range(10):
            lines = self.slight_mismatch(lines)
            lines = self.indentd_afterind(lines)
            lines = self.indent_afterind(lines)


        self.printer(lines)
        self.writeFile(lines,file1)
        print("")

    def firstline(self,lines):
        count = self.count_indentation_level(lines[0])
        lines[0] = self.isitindented(lines[0],0)
        return lines

    def check(self, window, windowindenters):
        if window[0] == window[2] and window[1] != window[1] and windowindenters[1] != 1:
            return True
        else:
            return False

    def check1(self, window, windowindenters):
        if window[1] != window[2] and window[1] % 4 != 0:
            return True
        else:
            return False

    def removeblanklines(self, lines):
        reachedend = False
        notencountered = True
        while not reachedend:
            for line in lines:
                notencountered = True
                for ch in line:
                    if ch != ' ' or ch != '\n':
                        # got character other than space and newline that means it is not a blank line
                        notencountered = False
                        break;
                if notencountered:
                    # it is a blank line
                    lines.remove(line)
                    break;
            if notencountered == False:
                reachedend = True
        return lines

    def indentd_afterind(self,lines):
        #detection section
        for i in range(0,len(lines)-1):
            foundindentr = False
            for j in self.indentstarters:
                if j in lines[i]:
                    foundindentr = True
                    break

            if foundindentr == False:
                currindentation = self.count_indentation_level(lines[i])
                nextindentation = self.count_indentation_level(lines[i+1])
                if nextindentation > currindentation:
                    lines[i+1] = self.isitindented(lines[i+1],currindentation)
        return lines

    def indent_afterind(self,lines):
        currindentation = 0
        for i in range(0,len(lines)-1):
            foundindentr = False
            for j in self.indentstarters:
                if j in lines[i]:
                    foundindentr = True
                    break
            if foundindentr == True:
                currindentation = self.count_indentation_level(lines[i])
                nextindentation = self.count_indentation_level(lines[i+1])


                if (currindentation < nextindentation) and currindentation != (nextindentation-4):
                    k = i+1

                    reindenteddone = False
                    tobeindented = nextindentation
                    toindented = currindentation+4
                    while(not reindenteddone):
                        temp = self.count_indentation_level(lines[k])
                        if temp == tobeindented:
                            lines[k] = self.isitindented(lines[k],toindented)
                        else:
                            reindenteddone = True
                        k+=1
                if (currindentation >= nextindentation) and currindentation != (nextindentation-4):
                    k = i+1

                    reindenteddone = False
                    tobeindented = nextindentation
                    toindented = currindentation+4
                    while(not reindenteddone):
                        temp = self.count_indentation_level(lines[k])
                        if temp == tobeindented:
                            lines[k] = self.isitindented(lines[k],toindented)
                        else:
                            reindenteddone = True
                        k+=1
        #return lines
        #self.printer(lines)
        return lines

    def slight_mismatch(self, lines):
        window = []
        window_lines = []
        window_indenters = []
        new_lines = []
        # initating window
        i = 0
        for t in range(10):
            while i < self.windowlength:
                indenterfound = False
                for j in self.indentstarters:
                    if j in lines[i]:
                        indenterfound = True
                        break
                    else:
                        indenterfound = False
                if indenterfound:
                    window_indenters.append(1)
                else:
                    window_indenters.append(0)
                window.append(self.count_indentation_level(lines[i]))
                i += 1
            #self.addreport(window)
            i = self.windowlength
            while i < len(lines):
                window.pop(0)
                window_indenters.pop(0)
                indenterfound = False
                for j in self.indentstarters:
                    if j in lines[i]:
                        indenterfound = True
                        break

                if indenterfound == True:
                    window_indenters.append(1)
                else:
                    window_indenters.append(0)

                window.append(self.count_indentation_level(lines[i]))
                if self.check1(window, window_indenters):
                    lines[i - 1] = self.isitindented(lines[i - 1], window[2])
                    pass
                i += 1
        return lines


    def isitindented(self, line, requiredspaces):
        actualspaces = 0
        for i in line:
            if i == ' ':
                actualspaces += 1
            else:
                break

        if (requiredspaces - actualspaces) > 0:
            line = ' ' * (requiredspaces - actualspaces) + line

        elif (requiredspaces - actualspaces) < 0:
            remo = (actualspaces - requiredspaces)
            while remo > 0:
                line = line[1:]
                remo -= 1
        return line

    def listtostring(self, lines):

        file = ""
        for i in lines:
            file += i + '\n'
        return file


    def count_indentation_level(self, line):
        count = 0
        for i in line:
            if i == ' ':
                count += 1
            else:
                break
        return count
        pass

    def findsection(self, linenos, lines):
        start = linenos - 1
        start_indent = self.count_indentation_level(lines[start])
        linenos += 1
        secondline = False
        secondend = 0;
        for lineindex in range(linenos, len(lines)):

            if secondline == False:
                if start_indent / 4 < self.count_indentation_level(lines[start]) / 4 and self.count_indentation_level(
                        lines[start]) % 4 == 0:
                    pass
                # indentation check for secondline is finished
                secondline = True

    def detect_indentation(self, lines):
        sectionfinder = []

        level = 0
        linenos = 1
        tenement = False
        irregular_identated_lines = []

        for line in lines:
            spacecount = self.count_indentation_level(line)

            if tenement == True:
                tenement = False
                level += 1

            for starter in self.indentstarters:
                if starter in line:
                    if self.count_indentation_level(line) % 4 == 0:
                        self.findsection(linenos, lines)
                    else:
                        self.addreport("error @ line ", linenos)
                    tenement = True
                    break

            #self.addreport(linenos, "   ", level * 4, spacecount, line)
            linenos += 1

        #self.addreport(irregular_identated_lines)


if __name__ == "__main__":
    p = Process("testfile")
