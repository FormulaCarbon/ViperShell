import os

#change this to the address of the file of your python stuff. replace all \ with /
projectFolder = "C:/Users/siddh/Documents/Python_projects/"
#Change this to change commandline prompt
prompt = "-->"

while 1:
    x = input(prompt)
    if x == 'quit':
        break
    if 'read' in x:
        filename = x[5:]
        filePath = projectFolder+filename
        print("Opening "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        print(file.read())
        file.close()
    if "run" in x:
        filename = x[4:]
        filePath = projectFolder+filename
        print("Executing "+filename+"...")
        file = open(filePath, "r")
        print("\n")
        exec(file.read())
        file.close()
    else:
        try:
            y = eval(x)
            if y: print(y)
        except:
            try:
                exec(x)
            except Exception as e:
                print ("error:", e)
