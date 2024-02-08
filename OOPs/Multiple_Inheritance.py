class ParentOne:
    def property_1(self):
        return "This is property 1."

    def property_2(self):
        return "This is property 2."


class ParentTwo:
    def property_3(self):
        return "This is property 3."

    def property_4(self):
        return "This is property 4."


class ChildOne(ParentOne, ParentTwo):
    def property_5(self):
        return "This is property 5"

    def property_6(self):
        return "This is property 6"


child_class_instance = ChildOne()

print(child_class_instance.property_1())    # Output: This is property 1. (Inherited from ParentOne)
print(child_class_instance.property_2())    # Output: This is property 2. (Inherited from ParentOne)
print(child_class_instance.property_3())    # Output: This is property 3. (Inherited from ParentTwo)
print(child_class_instance.property_4())    # Output: This is property 4. (Inherited from ParentTwo)
print(child_class_instance.property_5())    # Output: This is property 5. (Defined in ChildOne)
print(child_class_instance.property_6())    # Output: This is property 6. (Defined in ChildOne)

# In this code:
#
# ChildOne inherits from both ParentOne and ParentTwo.
# Instances of ChildOne have access to methods defined in both parent classes as well as its own methods.
# When calling property_1() and property_2(), the methods are inherited from ParentOne.
# When calling property_3() and property_4(), the methods are inherited from ParentTwo.
# property_5() and property_6() are defined within ChildOne.