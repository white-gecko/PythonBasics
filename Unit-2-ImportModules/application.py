#!/usr/bin/env python3

# This is your main file.
# If this file is called all the code written in de top level is executed

print ("The application was loaded")

import module

ourObject = module.OurClass()

print(ourObject.aProperty)

import SomeOtherModule

otherObject = SomeOtherModule.SomeOtherClass(ourObject)
