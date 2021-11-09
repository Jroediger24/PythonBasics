if 5>2:
 print ("hello, world!")
x=5
if x==5:
    y=10
print (x+y)
#this is a comment
t= 8 # x is now part of type int
t= "computer" # t is now part of typ str
print (t)
x= str(3)
y= int(3)  #variable names are case-sensitive
z= complex(3) #other type is float, which is decimals, scientific, and powers
print (z); print (x); print (y)
print(type(z));print (type(y));print (type(x))
a= 4; A="CAPITAL" #A will not overwrite a
print(a); print(A)
Myvariablename= 9 #variable names cannot use "-" or spaces
print (Myvariablename)
a, b, c= "large", "medium", "small"
print (b)
B=D=C = "library"
print (D)
print (D+A+a)
def myfunc():
    b="not medium" #you can create a temporary variable as long as it is within a function
    print(b+a)           #these are called local variables
                         #"a" is a global var in this situation
myfunc()
print (type(z))
