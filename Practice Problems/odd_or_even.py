#ask user for number
#print out if the number is even or odd
#BONUS: if number is divisible by four print out a different message

first_num = int(input("Number to check if odd/even: "))
if first_num%4 == 0:
    print("Even, and divisible by 4")
elif first_num%2 == 0:
    print("Even")
elif first_num%2 == 1:
    print("Odd")

#BONUS2: ask number for two numbers: 1)number to check (num) 2)number to check divisibility (check)

num = input("Enter a number to check: ")
check = input("Is " +num+" divisible by this:")
num = int(num)
check = int(check)
if num%check == 0:
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is not divisible by " + str(check))