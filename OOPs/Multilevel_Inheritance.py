class ParentClass:                      # LEVEL ONE
    def property_1(self):
        return "This is property 1."

    def property_2(self):
        return "This is property 2."


class ChildOne(ParentClass):            # LEVEL TWO
    def property_3(self):
        return "This is property 3"

    def property_4(self):
        return "This is property 4"


class GrandChild(ChildOne):             # LEVEL Three
    def property_5(self):
        return "This is property 5"

    def property_6(self):
        return "This is property 6"


grand_child_class_instance = GrandChild()

print(grand_child_class_instance.property_1())   # Output: This is property 1. (Inherited from ParentClass)
print(grand_child_class_instance.property_2())   # Output: This is property 2. (Inherited from ParentClass)
print(grand_child_class_instance.property_3())   # Output: This is property 3 (Inherited from ChildOne)
print(grand_child_class_instance.property_4())   # Output: This is property 4 (Inherited from ChildOne)
print(grand_child_class_instance.property_5())   # Output: This is property 5 (Defined in GrandChild)
print(grand_child_class_instance.property_6())   # Output: This is property 6 (Defined in GrandChild)

# In the code:
#
# ParentClass is the base class.
# ChildOne is a subclass of ParentClass.
# GrandChild is a subclass of ChildOne.
# GrandChild inherits properties from both ParentClass and ChildOne, and it also defines its own properties.