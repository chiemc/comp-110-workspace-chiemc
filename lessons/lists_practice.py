"""Basic syntax of lists."""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# add an item to the list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)

# create an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
last_game: int = game_points[2]
# modifying elements, can't do this with strings
game_points[1] = 72
print(game_points)

# getting the length
print(len(game_points))

# removing items
game_points.pop(2)
print(game_points)

# write a function called display
# input: list[int]
# RV: None
# loop over the input and print every value
# try calling it on game points


def display(input: list[int]) -> None:
    index_tracker: int = 0
    while index_tracker < len(input):
        print(input[index_tracker])
        index_tracker += 1
    return None


print(display(game_points))
