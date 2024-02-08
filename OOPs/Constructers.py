class Students:
    def __init__(self, name, age, class_, school):           # constructors
        self.student_name = name
        self.student_age = age
        self.student_class = class_
        self.student_school = school


student_class_Instance = Students("Saifullah", 18, 11, "APS")
print(student_class_Instance.student_name)
print(student_class_Instance.student_age)
print(student_class_Instance.student_class)
print(student_class_Instance.student_school)
