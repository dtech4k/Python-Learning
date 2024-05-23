# ask for input number, output all divisors of number
num = int(input("Input number:"))
if num<=0:
    print("Invalid Argument.")
    exit()

working = range(1, num+1)
output = []
for i in working:
    if num%i == 0:
        output.append(i)

for i in output:
    print(i)