count = [1, 2, 3, 4, 5, 7]
stonks = ["aa", "bb", "cc"]
random_things = ["puppies", 55, "antony", 1/2,["oh no", "a list inside a list"]]
# for loop gose throug list

for number in count:
	print("this is count",number)
# smae as above
for stock in stonks:
	print("big stonks in",stock)
# we can go throug mixed lists too
for i in random_things:
	print("some thing random = ",i)

# build lists
people = []

people.append("mat")
people.append("sara")
people.append("chris")
print(people)

people.remove("sara")
print(people)

for person in people:
	print("person is:",person)

# accses stuff from liwst
animals = ["bear", "dog","mamal", "tiger"]
print(animals[0])
print("list leght =", len(animals))
print(type(animals))
#The position of things in a list starts at 0, so to get the first thing you do [0].
#You can go backwards through the list using negative numbers. The last thing in a list is always [-1].

while
