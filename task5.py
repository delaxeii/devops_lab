#!/usr/bin/env python

# Start coordinate
robot = input("Robot movement: \n")
x = 0
y = 0

# Robot movement
for m in robot:
    if m == 'L':
        x -= x
    elif m == 'R':
        x += x
    elif m == 'U':
        y += y
    elif m == 'D':
        y -= y
    else:
        y -= y

# Output
print("Circular motion:\n", (x == 0 and y == 0))
