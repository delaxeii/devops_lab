#!/usr/bin/python3

# Start coordinate
robot = input("Robot movement: \n")
x = 0
y = 0

# Robot movement
for m in robot:
    if m == 'L':
        x = x - 1
    elif m == 'R':
        x = x + 1
    elif m == 'U':
        y = y + 1
    elif m == 'D':
        y = y - 1
    else:
        y = y - 1

# Output
print ("Circular motion:\n", (x == 0 and y == 0))
