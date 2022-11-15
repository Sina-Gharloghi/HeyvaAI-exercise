# create a tuple
animals = ("lion", "cat", "tiger", "horse")

print(animals , "\n",type(animals))

# loop
for x in animals:
    print ("animal = " , x)

# update a tuple
animals = list(animals)

animals.append("goat")

animals = tuple(animals)
print(animals , "\n",type(animals))

