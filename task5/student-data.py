student_data = {}
student_data["name"]= []
student_data["name"] = input("Please enter student's name: ")
courseNumber = int(input("Please enter the number of courses: "))
student_data["modules"]=[]

for i in range (courseNumber):
  module = {}
  module["coursename"] = input("Please enter the course: ")
  module["grade"] = int(input ("please enter the grade: "))
  student_data["modules"].append(module)
  print (student_data["name"], student_data["modules"])
#moduleno = int(input("Please enter the number of module: "))
'''while moduleno != int:
  print (input("Please enter an integer: "))
student_data["coursename"] = input("Please enter coursename: "

'''

