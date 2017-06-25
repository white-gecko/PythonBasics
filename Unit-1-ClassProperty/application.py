#!/usr/bin/env python3

# This is a class definition.
# When this file is called, the code within the class is not executed, the class is only *defined*
# (By convention the name of a class allways start with a capital letter)
class OurClass :

    # This is a proeprty of the class.
    # A property is a value which can be assoziated to an object (see below about the relation between class and object)
    # (By convention the name of a property always starts with a lower case letter)
    # The default value of this property is set to "default"
    aProperty = "default"

# The following code is directly executed when this file is called
print("Hello Beautyfull World!")

ourObject = OurClass()

print("The default value of our property is:", ourObject.aProperty)

ourObject.aProperty = "changed value"

print("The changed value of our property is:", ourObject.aProperty)
