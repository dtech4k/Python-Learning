#interestingly, lists can contain different data types, a well as size of the list isn't declared at initialization
bicycles = ['trek', 'cannondale', 'schwinn', 5]
print(bicycles)

#now how do we work with items in a list? selecting items is traditional, insofar as first index is number 0, and the index is selected with <listName>[<indexNumber>]
print(bicycles[0], bicycles[3])
#toreturn last item (i.e counting from the right, use negatives), -1 returns rightmost index
print(bicycles[-1], bicycles[-3])
#can use elements from list in f functions
numBikes = f"{bicycles[-1]} {bicycles[0]}"
print(numBikes,"bikes for sale.")

#manipulating elements in a list
motorcyles = ['honda','yamaha','ducati']
print(motorcyles)
# the .append() method adds the argument to the end of a list, however, only one argument at a time
motorcyles.append('harley')
print(motorcyles)

#elements can be inserted using the method .insert(n, 'element') where n==the desired index, and 'element' is the element which should go there, this then shifts everything else
#up an index (i.e. motorcycles[0] becomes motorcycles[1] etc)
motorcyles.insert(0, 'triumph')
#can also use .remove('element') method to remove a specific element 
#use of the del statement followed by list and index will delete the element at the desired index, and then resize the list
del motorcyles[2]
# .pop() method is built into python, removes last item from a list, and returns it
popped = motorcyles.pop()
print(motorcyles, popped)


#lists can be sorted using the .sort() method, when the argument reverse==True is passed in, alphabetical returns reverse alphabetical,
#interestingly, the boolean True must be capitalized
motorcyles.sort()
print(motorcyles)
motorcyles.sort(reverse=True)
print(motorcyles)
#also interestingly, the method return doesn't appear to work inside of a print() arg, which honestly, for me is kinda nice, allows for good readability imo

#a temporary sort, i.e. only the return of the method is sorted, can be put inside of a print statement

cars = ['toyota', 'honda', 'lexus', 'subaru']
print(sorted(cars))
print(cars)

#to reverse the order of a list, the .reverse() method can be invoked
cars.reverse()
print(cars)

#len() function returns int of the length of the list, the function requires the list to be passed in as the arg
print(len(cars))
numCars = len(cars)
print(numCars)