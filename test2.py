import re
def readfile(name):
    file = open(name, 'r', encoding = 'utf-8')
    fileread = file.read()
    file.close()
    return fileread

def numberline(fileread):
    fileread = fileread.splitlines()
#    print(fileread)
    for num,line in enumerate(fileread):
        if '/teiHeader' in line:
            namexml = num + 1
#            print(namexml)
    return str(namexml)

def writefile(first, name):
    filew = open(name, 'w', encoding = 'utf-8') 
    filew.write(first) 
    filew.close()

writefile(numberline(readfile('f.xml')),'first.txt')

def arrlemma(fileread):
    arr = re.findall('<w lemma=".*" type=".*">.*</w>',fileread)
#    print(arr)
    return arr

def makingdict(arr,fileread):
    d = {}
    for elem in arr:
        d[elem] = fileread.count(elem)
    return d

def second(d):
    second=''
    for key in d:
        second = second + key + '\t(Количество вхождений: ' + str(d[key]) + ')' + '\n'
#    print(second)
    return second

writefile(second(makingdict(arrlemma(readfile('f.xml')),(readfile('f.xml')))), 'second.txt')

def adj(fileread):
    reg = '<w lemma=".*" type="l.f.*"'
    adj = re.findall(reg,fileread)
#    print(adj)
    numadj = str(len(adj))
#    print(numadj)
    return numadj

writefile(adj(readfile('f.xml')),'third.txt')
