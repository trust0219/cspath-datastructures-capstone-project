from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py

# Inserting all the food type information into one Trie
origin = Trie()
for ft in types:
    origin.insert(ft)


# Write code to insert restaurant data into a data structure here. The data is in data.py
restaurant_table = HashMap(len(types))
for ft in types:
    ll_hashmap = LinkedList()
    for r in restaurant_data:
        if r[0] == ft:
            r_info_hashmap = HashMap(4)
            r_info_hashmap.assign("name", r[1])
            r_info_hashmap.assign("price", r[2])
            r_info_hashmap.assign("rating", r[3])
            r_info_hashmap.assign("address", r[4])
            ll_hashmap.insert_beginning(r_info_hashmap)
    restaurant_table.assign(ft, ll_hashmap)

# Write code for user interaction here
while True:
    user_input = str(
        input(
            "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n=> "
        )
    ).lower()
    # Search for user_input in food types data structure here
    list_food_types = origin.user_food_type(user_input)
    if len(list_food_types) > 1:
        print(list_food_types)
        print("Please continue until there is one specific food type, let's try again!")
        continue
    elif len(list_food_types) == 0:
        print("We can't find {0}. Please try again".format(user_input))
        continue
    else:
        user_input = str(
            input(
                "\nThe only option with those beginning letters is {0}. Do you want to look at {0} restaurants? Enter 'y' for yes and 'n' for no.\n=> ".format(
                    list_food_types[0]
                )
            )
        ).lower()
    if user_input == "n":
        continue
    # After finding food type write code for retrieving restaurant data here
    restaurant_list = restaurant_table.retrieve(list_food_types[0])
    curr = restaurant_list.get_head_node()
    while curr.get_next_node():
        r_info_hashmap = curr.get_value()
        print("------------------\n")
        print("Name: {}".format(r_info_hashmap.retrieve("name")))
        print("Price: {}/5".format(r_info_hashmap.retrieve("price")))
        print("Rating: {}/5".format(r_info_hashmap.retrieve("rating")))
        print("Address: {}\n".format(r_info_hashmap.retrieve("address")))
        print("------------------\n")
        curr = curr.get_next_node()

