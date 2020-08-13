'''
Understand:


My Plan:
create a dictionary of 500 rooms 0 - 499 with an exmple being - 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}

set up a queue for function runs
create a visited

possiblly a while loop for the length of the amount of rooms being added to vistied.
    set a current and previous room to starting room
    have player enter starting room and check the exits
        for loop for possible directions
            if an exit in a direction does not exist it removes it from the dictionary
        for loop for remining unchecked directions
            move player into a new room
            change current to the new room id
            add to visited
            change previous room's direction in dict to current room id
            change current room's opposite direction in dict to previous room id
            add in queue to run function again with the current room as the starting room
            move player in oposite direction back to previous room
            reset current room to previous room
        

'''