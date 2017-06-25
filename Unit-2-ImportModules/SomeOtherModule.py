#!/usr/bin/env python3

print ("The other module was loaded")

class SomeOtherClass :

    object = None

    def __init__(self, object):
        print("SomeOtherClass")
        self.object = object


    def someMethod(self) :
        print("some Method is executed, object is:", self.object)
