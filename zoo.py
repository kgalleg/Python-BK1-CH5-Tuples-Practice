#python tuples - Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

# Instructions
# Create a tuple named zoo that contains 10 of your favorite animals.
# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1

zoo = ("bear", "tiger", "giraffe", "zebra", "monkey", "snake", "unicorn","bird", "lion", "elephant")
print(zoo.index("unicorn"))

# Determine if an animal is in your tuple by using value in tuple syntax.

# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found

animal_to_find = "kangaroo"
if animal_to_find in zoo:
    print("animal found")
else:
    print("animal not found")


# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.

(first_child, second_child, third_child, fourth_child, fifth_child, sixth_child, seventh_child, eight_child, nineth_child, tenth_child) = zoo

print(first_child)
print(second_child)
print(third_child)
print(fourth_child)



# Convert your tuple into a list.
#this is a tuple
zoo = ("bear", "tiger", "giraffe", "zebra", "monkey", "snake", "unicorn","bird", "lion", "elephant")

#converting tuple into a list:
tuple_list = list(zoo)
print ("list elements: ", tuple_list)


# Use extend() to add three more animals to your zoo.
#adding a variable and 3 animals I will add to zoo
more_animals = ["penguin", "panda", "hippo"]

#my zoo list adding more_animals variable
tuple_list.extend(more_animals)

print('new zoo list:', tuple_list)


# Convert the list back into a tuple.
newest_zoo_tuple=tuple(tuple_list)

print("newest zoo tuple", newest_zoo_tuple)






