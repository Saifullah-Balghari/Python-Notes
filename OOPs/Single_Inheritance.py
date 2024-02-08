class ParentClass:
    def property_1(self):
        return "This is property 1."

    def property_2(self):
        return "This is property 2."


class ChildOne(ParentClass):
    def property_3(self):
        return "This is property 3"

    def property_4(self):
        return "This is property 4"


child_class_instance = ChildOne()

print(child_class_instance.property_1())    # child class got property_1 and _2 from parent class
print(child_class_instance.property_2())    # along with its own properties
print(child_class_instance.property_3())
print(child_class_instance.property_4())
