                    #文件路径
keywords=['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
          'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed',
          'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'unsigned', 'void', 'volatile', 'while']
alphabet=[1]*26
words= [0]*50
str1=''
a=j=b=count=0
for i in range(0,26):
    alphabet[i] = chr(97+i)       #建立一个list来储存字母
    i+=1
print(alphabet)
with open("lll.txt","r") as f:          #读取文件
    lines = f.readlines()
    #将文件中所有的单词提取出来

    for line in lines:                  #每一行
        line = line.strip()     #消除每行前后面的空格
        line = line.replace("#","")
        print(line)
        for n in range(0,len(line)):       #在line长度之内

            if (line[n]==alphabet[j]):       #line中某个元素是26个小写字母
                str1=str1+line[n]               #将line中的每个字母写入一个string当作单词
                print(line[n])
                print(str1)
                n+=1                        #下一位
                j=0

            elif j+1==26:                  #不是26个小写字母
                words[b]=str1

                str1=''             #重置string
                b+=1
                j=0                        #将j初始化
                n+=1                      #继续遍历
            elif (j+1)!=26:              #还没找到26中的一个
                # 下一个字母
                j+=1

    for word in words:
         for key in keywords:
             if word == key:
                count+=1

    print("number of keyword is: ",count)

# 二级命令
with open("lll.txt","r") as f:          #读取文件
    lines = f.readlines()
    #将文件中所有的单词提取出来
    switchNum = 0
    caseNum = 0
    case = []
    key1 = 'switch'
    key2 = 'case'
    space = 0
    num = 0

    for line in lines:
        num += 1
        space = line.find(key1)
        if space != -1:
            for line in lines[num:]:
                if line.find(key2) != -1:  # 当找到了“case”，是正确的，不等于-1
                    caseNum += 1
                if line.find('}') == space:
                    switchNum += 1
                    case.append(caseNum)
                    caseNum = 0
                    break

#三级命令
num = 0
ifElseNum = 0
ifElseifElseNum = 0

with open("lll.txt","r") as f:          #读取文件
    lines = f.readlines()
    for line in lines:
        num += 1
        if 'if' in line and 'else if' not in line:
            ifSpace = line.find('if')

            for line in lines[num:]:
                if 'else' in line and ifSpace == line.find('else'):
                    if 'else if' in line:

                        ifElseifElseNum+= 1
                    else:

                        ifElseNum += 1
                    break
    print(totalNum, switchNum, case, ifElseNum, ifElseifElseNum)

#四级命令
with open("lll.txt","r") as f:          #读取文件
    lines = f.readlines()
    for line in lines:
        num += 1
        if 'if' in line and 'else if' not in line:
            ifSpace = line.find('if')

            for line in lines[num:]:
                if 'else' in line and ifspace == line.find('else'):
                    if 'else if' in line:

                        ifElseifElseNum += 1
                    else:

                        ifElseNum+= 1
                    break
    print(totalNum, switchNum, case, ifElseNum, ifElseifElseNum)
