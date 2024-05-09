#tuples are immutable lists, immutable being values that cannot be changed
#tuples are defined with parentheses() instead of brackets[]
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#python will not allow you to overwrite the values at given indeces when they're contained within a tuple
# => dimensions(0)=10 doesn't work

#however! while the tuple itself can't be manipulated, the variable can be overwritten with a new tuple object, allowing the garbage collector to destroy the previous one
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

dimensions.append(5)
print(dimensions)