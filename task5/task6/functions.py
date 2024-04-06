#functions
def yo (a):
    return a * 2
print (yo (3))
def studentInfo ():
    print ("what would you like to do?")
    print("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    choice = input ("Type one letter (a/v/q):").strip()
    return choice
choice = studentInfo()
print (f"you chose {choice}")

def doAdd():
    print ("In adding")
def doView():
    print ("in viewing")
#main program
choice = studentInfo()
while choice != "q":
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView ()
    elif choice != "q":
        print ("\n \n Please select either a,v or q")
        choice = studentInfo
        print (choice)
