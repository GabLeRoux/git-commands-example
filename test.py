#!/usr/bin/env python

for x in [y**2 for y in range(10)]:
    if (x < 5):
        print((x, "x smaller than 5"))
    else:
        print((x, "x greater than 5"))

