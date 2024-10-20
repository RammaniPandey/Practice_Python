#Students = ["Ram","Syamm","Radha","Mohan","Kajal"]
#houses = ["Padari","Padari","Padari","mukundpure","tala",]
Students = {
    "Ram":"Padari","Syamm":"mukundpure",
    "Radha":"tala","Mohan":"Rewa",
    "Kajal":"Satna","Anshu":"Amarpatan", 
    }
#print(Students["Ram"])
#print(Students["Anshu"])
for Student in Students:
    print(Student, Students[Student], sep=", ")