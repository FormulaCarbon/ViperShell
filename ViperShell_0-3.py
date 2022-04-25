import os
from colored import fg
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
VSSettings.close()
print("\n")
print("ViperShell v0.3 Started. What would you like to do? Use v//:? for a list of commands")

while 1:
    x = input(prmptcolor+prompt+resetcolor)
    
    if x == 'v//:quit':
        VSSettings.close()
        break
    if 'v//:read' in x:
        filename = x[9:]
        filePath = projectFolder+filename
        print("Opening "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        print(file.read())
        file.close()
    if "v//:run" in x:
        filename = x[8:]
        filePath = projectFolder+filename
        print("Executing "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        exec(file.read())
        file.close()
    if x == "v//:?":
        print("Opening help menu... \n\n")
        print(" v//:quit: exit ViperShell \n v//:read prgmName.py: display contents of a program \n v//:run prgmName.py: run a program\n v//:?: list commands \n v//:fileslist: list files in directory")
    if x == "v//:filelist":
        print("Displaying file names in directory"+projectFolder+"...\n\n")
        filelist = os.listdir('C:/Users/siddh/Documents/Python_projects/')
        print(filelist)
    if x == "v//:cmdprmpt":
        askprmpt = input('Please type new command prompt: ')
        askcolor = input('Please type new prompt color: ')
        VSSettings=open(projectFolder+'VSSettings.txt', mode='w')
        VSSettings.write(password + '\n' + username + '\n' + askprmpt + '\n' +askcolor)
        print('Restart ViperShell to see changes')
    else:
        try:
            y = eval(x)
            if y: print(y)
        except:
            try:
                exec(x)
            except Exception as e:
                print ("error:", e)
