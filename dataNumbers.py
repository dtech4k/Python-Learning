#fun fact: don't call this numbers.py or it'll try to overload the actual numbers.py lib

#integers
x=5
y=2
z = x-y
print(z)

#again interestingly, you don't have to declare data type when initializing a variable in python, there's a lot going on under the hood here

#python also supports the tradition +,-,/ operators
print(x/y)
print(4/2)
#python also converts from integer to float in any instance of the / operator
#lets see how nice these data types play with one another, seems that all defaults to float, which makes a lot of since, as there's no flag to convert back to int
print(2.0+2)
#type casting time
#python will truncate whenever type casting from float to int
print(int(2.0),int(2.7))
#the underscore in big numbers is a handy readability tool
bigNumber = 2_000_000

#python supports multiple assignments, across types as well
a, b, c = 1, 2, 3.0
print(b+c)

#when establishing a var as a CONSTANT, use all caps, no hardcoded protection, but conventionally protects
FINALNUMBER=9
FINALNUMBER=FINALNUMBER-3
print(FINALNUMBER)
