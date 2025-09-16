import sys
if len(sys.argv) != 2:
    print("none")
else:
    sentences = sys.argv[1]
    counter = 0
    for char in sentences:
        if char == "z":
            counter += 1
    
    if counter > 0:
        print("z" * counter)
    else:
        print("none")