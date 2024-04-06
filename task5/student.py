student = {
    "name": "Mary",
    "modules": [
        { 
            "coursename":"programming",
            "grade": 45
        }, 
        {
            "coursename": "History", 
            "grade": 99
        }
        ]
        }
print (f"student: {student['name']}")

for module in student ["modules"]:
    print ("\t {} \t: {} ".format(module ["coursename"], module ["grade"]))

student = {input ("Enter student's name: ")}

#{input("Enter modules: coursename {}: grade {})