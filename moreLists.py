#for loops
magicians = ["alice", "bob", "david", "carolina"]
for magician in magicians:
    print(magician)
#the use of the colon and indents for the for loops is interesting, but the format of for (magician : magicians) is similar to java (except java uses those parentheses)
for magician in magicians:
    print(f"{magician.title()}","that was a great trick!")

#using lists for numbers

#range() function, generates a series of numbers between the first and second arg
#left side is inclusive and right side is exclusive [x,y)
for value in range(1,5):
    print(value)

#if counting from 0, the range with a single argument (being the right hand exclusive endpoint)
for value in range(6):
    print(value)

#the range() function can be used to generate lists
#the list itself is generated differently from before, this time the list() function is invoked
number = list(range(1,6))
print(number)

#range() function is pretty flexible, when passed in three numerical arguments (x, y, n) x==left hand inclusive endpoint, y==right hand exclusive endpoint, n==increment
evenNumbers=list(range(2,11,2))
print(evenNumbers)

#can generate an empty list and populate with the .append() method, also of note ** indicates exponents
squares= []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

#the min(), max(), sum() functions all work with lists of numbers to return the applicable numbers
smallSquare = min(squares)
bigSquare = max(squares)
allSquare = sum(squares)

print(smallSquare, bigSquare, allSquare)

#new hotness: list comprehensions, basically the ability to populate a list by using a for loop inside of the list brackets
squares2=[value**2 for value in range (1,11)]
print(squares2)



##slicing a list
#pieces of a list can be partitioned out by indicated the leftmost index(incl.) and the rightmost(excl.)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#however, when beginning from the first index, the 0 can be ommited
print(players[:3])

#when declaring a start index through to the end, a similar scheme is used:
print(players[3:])

#the negative index technique still works when workes with slices of a list:
print(players[-3:]) 

#slices can also be looped through with for loops:
print("here are the first three players on my team")
for player in players[:3]:
    print(player.title())

##copying a list:
my_foods = ['pizza', 'falafel', 'carrot cake']
#this is so interesting! when the list is followed by the [:] it creates a new object, however when that is ommitted the address of the object is simply assigned to 
#the new variable
friend_foods = my_foods[:]
#side note: it appears that snake_case is preferred in python rather than camelCase
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)