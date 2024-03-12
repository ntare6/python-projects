#list are mutable

chocolate=["vanilla","coffe","strawberry","milk"]

chocolate[0:2]=["tomatoes of nyirangarama"]

print("your chocolate is now",chocolate)

schools=["auca","uk","ulk","ur","iprc","east africa"]

del schools[1]

print("your schools are now",schools)

#deleting a slice

teams=["man utd","chelsea","arsenal","real madrid","liverpool"]

del teams[2:]

print("your team is now",teams)

#nested list
nested=["first",("second","third"),["fourth","fifth"]]

print("the nested list is",nested)

#better way

new=[("isaac",10),("tony",12),("aime",13)]

print(new)

#to access one of the elements of one of the tuples

new_name=new[2]

print(new_name)

#to access aime

print(new[2] [0])


#unpacking

name,age=("me",45)
print(name)
print(age)
