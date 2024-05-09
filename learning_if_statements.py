#if statements are very familiar to me, let's see how these differ!
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#so following the scheme we noticed from the for loops, parentheses aren't used, but rather colons and indentation cover the formatting

#if statements often rely on comparison operators, and of note here is that the strings can be compared with the equality == operator, however, the == operator is case sensitive,
#so good practice should follow that <var>.lower() should be used to compare to a lowercase operator

#since the == operator works for strings, so too does the != operator
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print('hold the anchovies!')


#when working with numbers, the typical comparison operator works just as in java, however the use of && is taken over by simple use of the word and
age_0=22
age_1=18
if (age_0>=21) and (age_1<=21):
    print('and statement is true')

#similarly to the use of && as and, || becomes or
if(age_0>=21) or (age_1>=21):
    print("or statement is true")
#the simple comparison operators of <,>,==, etc take precedence in OOP before the and/or

#checking to see if a value is in a list:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}",'you may log in.')

#just like java, if statments come in three major flavors: simple if statements, if-else statements, if-elif-else statements
age = 12
if age<4:
    price=0
elif age <18:
    price = 25
elif age <65:
    price = 40
else:
    price = 25
#the else can be ommitted, just make sure the code is robust enought to hanbdle all cases.

toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in toppings:
    print('adding mushrooms')
if 'anchovies' in toppings:
    print('adding anchovies')
if 'extra cheese' in toppings:
    print('adding extra cheese')

# to check if a list is empty
requested_toppings = []
if requested_toppings:
    for request in requested_toppings:
        print(f"{request}","is being added.")
else:
    print("are you sure you want a plain pizza?")