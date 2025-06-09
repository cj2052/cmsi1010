import sys

moves_taken = 0
locations = {'disk 1': 'A', 'disk 2': 'A','disk 3': 'A'}
def move(n, source, destination, auxiliary):
    if n > 0:
        move(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        
        global moves_taken
        moves_taken += 1
        move(n - 1, auxiliary, destination, source)
      
try:
    if len(sys.argv) != 2:
        raise ValueError("Exactly one argument is required")
    if not sys.argv[1].isdigit():
        raise ValueError("The argument must be a positive integer")
    number_of_disks = int(sys.argv[1])
    if number_of_disks < 1 or number_of_disks > 20:
        raise ValueError(
            "The argument must be between 1 and 20, inclusive")
    move(number_of_disks, "A", "B", "C")
    print(moves_taken, "moves taken") 
except ValueError as e:
    print(f"Error: {e}")

# minimum number of moves per disk is n once, n-1 twice, n-2 four times, n-3 eight times, etc
# 1 disk = 1 move
# 2 disks = 3 moves
# 3 disks = 7 moves 
# 4 disks = 15 moves
# 5 disks = 31 moves
# 6 disks = 63 moves
# 7 disks = 127 moves 
# moves = 2(moves(disks-1)) + 1
