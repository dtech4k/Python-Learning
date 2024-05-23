import random
#take these two list output a new list that contains only elements that are in both lists
a = []
b = []
num = 10
while num > 1:
    a_add = random.randint(1,10)
    b_add = random.randint(1,10)
    a.append(a_add)
    b.append(b_add)
    num-=1

print(a)
print(b)

output = []

for i in a:
    if i in b:
        b_index = b.index(i)
        output.append(b.pop(b_index))

print(output)