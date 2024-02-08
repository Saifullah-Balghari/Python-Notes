class Parent:
    def property_1(self):
        return "This is property 1."

    def property_2(self):
        return "This is property 2."


class ChildOne(Parent):
    def property_3(self):
        return "This is property 3"

    def property_4(self):
        return "This is property 4"


class ChildTwo(Parent):
    def property_5(self):
        return "This is property 5"

    def property_6(self):
        return "This is property 6"


child_one_instance = ChildOne()
child_two_instance = ChildTwo()

print(child_one_instance.property_1())    # Output: This is property 1. (Inherited from Parent)
print(child_one_instance.property_2())    # Output: This is property 2. (Inherited from Parent)
print(child_one_instance.property_3())    # Output: This is property 3. (Defined in ChildOne)
print(child_one_instance.property_4())    # Output: This is property 4. (Defined in ChildOne)
print("\n")
print(child_two_instance.property_1())    # Output: This is property 1. (Inherited from Parent)
print(child_two_instance.property_2())    # Output: This is property 2. (Inherited from Parent)
print(child_two_instance.property_5())    # Output: This is property 5. (Defined in ChildTwo)
print(child_two_instance.property_6())    # Output: This is property 6. (Defined in ChildTwo)

# In this example:
#
# ChildOne and ChildTwo both inherit from Parent, forming a hierarchical structure.
# Instances of ChildOne and ChildTwo have access to methods defined in Parent, as well as their own methods.
# ChildOne and ChildTwo share the same parent class but have different sets of methods defined within them.
