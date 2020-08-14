from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# setting up an inital dictionary with as many entries as there are rooms

# create a dictionary of 500 rooms 0 - 499 with an exmple being - 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
room_dict = {}
for x in range(0, len(room_graph)):
    room_dict[x] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# set up some sort of queue for function runs ######

# create a visited

poss_dirs = ['n', 's', 'e', 'w']
opposite_dirs = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

def sprint_slayer(current_room, visited=None):
    if visited == None:
        visited = set()
    visited.add(current_room.id)

    # possiblly a while loop for the length of the amount of rooms being added to vistied
    while len(visited) < len(room_graph):
        # set a current and previous room to starting room
        current = current_room
        previous = current_room

        # for loop for possible directions
        for direction in poss_dirs:
            # if an exit in a direction does not exist it removes it from the dictionary
            if direction not in current.get_exits():
                room_dict[current.id].pop(direction)
        
        # for loop for available directions
        for avail_exit in room_dict[current.id]:
            #check if direction goes to an unchecked room
            if room_dict[current.id][avail_exit] == '?':
                # move player into a new room
                player.travel(avail_exit)
                # change current to the new room
                current = player.current_room
                print()
                print(current)
                print()
                # add to visited
                visited.add(current.id)
                print()
                print(visited)
                print()
                # change previous room's direction in dict to current room id
                room_dict[previous.id][avail_exit] = current.id
                # change current room's opposite direction in dict to previous room id
                room_dict[current.id][opposite_dirs[avail_exit]] = previous.id
                # add in queue to run function again with the current room as the starting room

                # move player in oposite direction back to previous room
                player.travel(opposite_dirs[avail_exit])
                # reset current room to previous room
                current = previous


sprint_slayer(world.starting_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
