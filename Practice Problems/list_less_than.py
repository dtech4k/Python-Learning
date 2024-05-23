#take a list of ints
#write a program that prints out all elements that are less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
to_check = int(input("Enter a number: "))
output = []
for i in a:
    if i < to_check:
        output.append(i)
print(output)