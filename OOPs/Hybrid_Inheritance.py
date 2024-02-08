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


class ChildOne(ParentOne):
    def property_5(self):
        return "This is property 5"

    def property_6(self):
        return "This is property 6"


class ChildTwo(ParentOne, ParentTwo):
    def property_7(self):
        return "This is property 7"

    def property_8(self):
        return "This is property 8"


class GrandChild(ChildOne, ParentTwo):
    def property_9(self):
        return "This is property 9"


child_one_instance = ChildOne()
child_two_instance = ChildTwo()
grand_child_instance = GrandChild()

print(child_one_instance.property_1())    # Output: This is property 1. (Inherited from ParentOne)
print(child_one_instance.property_2())    # Output: This is property 2. (Inherited from ParentOne)
print(child_one_instance.property_5())    # Output: This is property 5. (Defined in ChildOne)
print(child_one_instance.property_6())    # Output: This is property 6. (Defined in ChildOne)

print(child_two_instance.property_1())    # Output: This is property 1. (Inherited from ParentOne)
print(child_two_instance.property_2())    # Output: This is property 2. (Inherited from ParentOne)
print(child_two_instance.property_3())    # Output: This is property 3. (Inherited from ParentTwo)
print(child_two_instance.property_4())    # Output: This is property 4. (Inherited from ParentTwo)
print(child_two_instance.property_7())    # Output: This is property 7. (Defined in ChildTwo)
print(child_two_instance.property_8())    # Output: This is property 8. (Defined in ChildTwo)

print(grand_child_instance.property_1())  # Output: This is property 1. (Inherited from ParentOne)
print(grand_child_instance.property_2())  # Output: This is property 2. (Inherited from ParentOne)
print(grand_child_instance.property_3())  # Output: This is property 3. (Inherited from ParentTwo)
print(grand_child_instance.property_4())  # Output: This is property 4. (Inherited from ParentTwo)
print(grand_child_instance.property_5())  # Output: This is property 5. (Inherited from ChildOne)
print(grand_child_instance.property_6())  # Output: This is property 6. (Inherited from ChildOne)
print(grand_child_instance.property_9())  # Output: This is property 9. (Defined in GrandChild)

# In this example:
#
# ChildOne inherits from ParentOne.
# ChildTwo inherits from both ParentOne and ParentTwo.
# GrandChild inherits from ChildOne and ParentTwo.
# ChildOne, ChildTwo, and GrandChild form a hybrid inheritance structure, where multiple inheritance and hierarchical inheritance are combined.
