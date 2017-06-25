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

# Now we create two instances of our class, an instance is also called object.
# A class is an abstract definition, while an object is an actuall thing which has the properties defined by the class
# (By convention also variables starts with a lower case letter)
ourObject = OurClass()
ourSecondObject = OurClass()

# We can access the properties of an object
print("The default value of 'aProperty' of 'ourObject' is:", ourObject.aProperty)
print("The default value of 'aProperty' of 'ourSecondObject' is:", ourSecondObject.aProperty)

# and we can change the properties of an object
ourObject.aProperty = "changed value"

print("The changed value of 'aProperty' of 'ourObject' is:", ourObject.aProperty)
print("The value of 'aProperty' of 'ourSecondObject' is still:", ourSecondObject.aProperty)
