#ask the user for a string and check if the string is a palindrome or not
userInput = input("Is your word a palindrome? Enter it here: ")
to_check = userInput.lower()
half_len = int(len(to_check)/2)
first = []
last = []
#i forgot about slicing a list
# list[x:y] means [start_index:end_index)
for c in to_check[:half_len]:
    first.append(c)
if len(to_check)%2 != 0:
    half_len+=1
for c in to_check[half_len:]:
    last.append(c)

for c in first:
    if c in last:
        continue
    else:
        print(userInput + " is NOT a palindrome.")
        exit()
print(userInput + " is a palindrome.")