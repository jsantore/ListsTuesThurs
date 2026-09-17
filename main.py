
courses = ["comp151", "Comp206", "Math130", "Math120",]
courses.append("Math161")
courses.insert(1, "Comp152")
courses[1] = "cybf210"
next_class = input("What class will you take next")
courses.append(next_class)
print(courses)
courses.remove ("Math161")
print(courses)
courses[6]="CYBF490"