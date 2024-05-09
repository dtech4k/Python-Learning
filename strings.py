print('Hello World!')

first = "ada"
last = "lovelace"
fullName = f"{first} {last}"

caps = "MFDOOM"
spell = "all caps"
#<string>.title() to upper first char in each string separated by space
print(fullName.title())
#similarly
print(first.upper())
print(caps.lower())

allCaps = f"{caps} {spell}"
print(allCaps.upper())

# .strip() method removes any blank space on left&&right sides
#if only one side is desired, invoke .lstrip() or .rstrip()

##removing prefixes:
nostarch_url = "https://nostarch.com"
print(nostarch_url)
print(nostarch_url.removeprefix("https://"))
#note: the .removeprefix() method does not actually alter the original variable, only RETURNS variable w/o prefix
# =>
short_url = nostarch_url.removeprefix('https://')
print(short_url)