file = open("/input1.txt", "r")

sum = 0

for line in file:
    number = ""
    # First digit
    for i, c in enumerate(line):
        if c.isdigit():
            number += c
            break

    # Second digit
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            number += c
            break
    
    sum += int(number)
    
print(sum)