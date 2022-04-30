## Mike Mallison, Comfy Deviations

import statistics
inp = 0

while inp != 1:
    counter = 0
    print("Enter the 10 numbers that are between 68 and 80 and are seperated by spaces:")
    inp = list(map(float, input().split()))
    for i in inp:
        counter = counter + 1
    while counter > 10:
        inp.pop()
        counter = counter - 1
        
    if statistics.stdev(inp) > 1.0:
        print("NOT COMFY")
    else:
        print("COMFY")
    print("")
    print("")
