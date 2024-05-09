## so from my understanding, outside of the simplicity of the language, the use of dictionaries is what makes python so useful
#dictionaries are one of the four data collection types in pythons
#dictionaries hold sets of key : value pairs, and are indicated by curly braces
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just scored",f"{new_points}","points!")

#dictionaries can be appended with new sets of key : value pairs
alien_0['x_coord']=0
alien_0['y_coord']=25
print(alien_0)

#alternatively you can start with an empty dictionary and fill as you go:
alien_1 = {}
alien_1['color']='yellow'
alien_1['points']=10
print(alien_1)

#the dictionary can be modified using if-elif-else etc statements
alien_0['speed']='medium'
if alien_0['speed']=='slow':
    x_increment =1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_coord']=alien_0['x_coord']+x_increment
print(f"New positions: {alien_0['x_coord']}")

#to remove key : value pairs use the del function
print(alien_0)
del alien_0['points']
print(alien_0)

#dictionaries can also be quieried:
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}
language = favorite_languages['sarah']
print(f"Sarah's favorite language is {language}.")

#if you want to look for a key that may or may not exist, best practice is to use the .get() method, it'll return whatever you pass in as the second argument should the key not exist
#since we deleted 'points' from alien_0 let's ask for that
point_value = alien_0.get('points', 'no point value assigned')
x_location = alien_0.get('x_coord', 'no x coord')
print(point_value)
print(x_location)
