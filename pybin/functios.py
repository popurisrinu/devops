#!/usr/bin/python

def add(x=10,y=1):
        return x+y
def printline():
        "This is procedure "
        print '#'*25
print "I'm in main now"

# Function call in an expression
x=add(100,3)+30
print "Expression       :", x

# Function call in assignment
y=add(50,50)
print "Assignment       :",y

# Function call in output
print "Output           :", add(200,300)
print "Default arguments:", add()
print "Partial arguments:", add(y=20)

# Procedure call
printline()


