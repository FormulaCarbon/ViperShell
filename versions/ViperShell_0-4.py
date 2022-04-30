import os
from colored import *
#change this to the address of the file of your python stuff. replace all \ with /
projectFolder = "C:/Users/siddh/Documents/Python_projects/"
VSSettings=open(projectFolder+'VSSettings.txt', mode='r')
lineNum = 0
lines = []
#0 - pass
#1 - user
#2 - prompt
#3 - prompt color
while lineNum<4:
    VSfile = VSSettings.readline()
    lines.append(VSfile.strip())
    lineNum = lineNum +1
password = lines[0]
username = lines[1]
prompt = lines[2]
prmptcolor = fg(lines[3])
resetcolor = '\033[0m'
errorHeaderColor = bg('red_1')+fg('white')
errorColor = fg('red_1') + bg('black')
VSSettings.close()
print("\n")
print("ViperShell v0.3 Started. What would you like to do? Use v//:? for a list of commands")

while 1:
    x = input(prmptcolor+prompt+resetcolor)
    
    if x == 'v//:quit':
        VSSettings.close()
        break
    elif 'v//:read' in x:
        filename = x[9:]
        filePath = projectFolder+filename
        print("Opening "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        print(file.read())
        file.close()
    elif "v//:run" in x:
        filename = x[8:]
        filePath = projectFolder+filename
        print("Executing "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        exec(file.read())
        file.close()
    elif x == "v//:?":
        print("Opening help menu... \n")
        print(" v//:quit: exit ViperShell \n v//:read prgmName.py: display contents of a program \n v//:run prgmName.py: run a program\n v//:?: list commands \n v//:fileslist: list files in directory\n v//:cmdprmpt: change command prompt\n v//:openEditor: open new file in IDLE editor")
    elif x == "v//:filelist":
        print("Displaying file names in directory "+projectFolder+"...\n\n")
        filelist = os.listdir('C:/Users/siddh/Documents/Python_projects/')
        print(filelist)
    elif x == "v//:cmdprmpt":
        askprmpt = input('Please type new command prompt: ')
        askcolor = input('Please type new prompt color: ')
        VSSettings=open(projectFolder+'VSSettings.txt', mode='w')
        VSSettings.write(password + '\n' + username + '\n' + askprmpt + '\n' +askcolor)
        print('Restart ViperShell to see changes')
    elif x == "v//:openeditor":
        print('Opening IDLE Editor...')
        os.startfile("C:\\Users\\siddh\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.py")
    else:
        try:
            y = eval(x)
            if y: print(y)
        except:
            try:
                exec(x)
            except Exception as e:
                error = str(e)
                print (errorHeaderColor +"Error:" + errorColor + ' ' + error + resetcolor)
