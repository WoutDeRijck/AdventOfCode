file = open("/input1.txt", "r")

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

sum = 0

def numberTextInString(substring):
    for key in numbers.keys():
            if key in substring:
                return numbers[key]
    return ""

for line in file:
    number = ""

    # First digit
    for i, c in enumerate(line):
        nr = numberTextInString(line[:i])
        if(nr != ""):
            number += nr
            break

        if c.isdigit():
            number += c
            break

    # Second digit
    for i, c in enumerate(line[::-1]):
        nr = numberTextInString(line[len(line)-i:])
        if(nr != ""):
            number += nr
            break

        if c.isdigit():
            number += c
            break

    sum += int(number)
    
print(sum)