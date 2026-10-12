from operator import truediv

sequence = str(input("Enter the sequence: "))
marker = str(input("Enter the character for the marker: "))
start = False
count = 0
for i in range(len(sequence)):
    if start and sequence[i] == marker:
        print(f"The distance between the markers is {count}")
    elif sequence[i] == marker:
        start = True
    elif start:
        count += 1
