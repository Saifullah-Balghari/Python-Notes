class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        return f"I am an instance method. Instance variable value: {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"I am a class method. Class variable value: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "I am a static method. No access to instance or class variables"


# Creating an instance of MyClass
obj = MyClass("Hello")

# Calling instance method
print(obj.instance_method())  # Output: I am an instance method. Instance variable value: Hello

# Calling class method
print(MyClass.class_method())  # Output: I am a class method. Class variable value: I am a class variable

# Calling static method
print(MyClass.static_method())  # Output: I am a static method. No access to instance or class variables

# n this example:
#
# instance_method is a regular instance method that takes self as its first parameter. It can access instance variables.
# class_method is decorated with @classmethod. It takes cls (the class itself) as its first parameter. It can access class variables.
# static_method is decorated with @staticmethod. It does not take any default parameters related to the instance or the class. It cannot access instance or class variables; it behaves like a regular function defined outside the class.
# class_variable is a class variable defined outside any method. It is accessible by both class methods and instance methods.
