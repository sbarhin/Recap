PyMp = 0
IsMp = 0
IsVoting = True
record = []
while IsVoting:
    name = input("Enter your name in full: ")
    for i in record[1::]:
        if name in record:
            print("You have voted")
            continue
    record.append(name)
    choice = int(input("1 for PyMp and 2 for IsMp: "))
    if choice == 1:
        PyMp += 1
    if choice == 2:
        IsMp += 1
    a = input("Any more voters? Y/N: ")
    if a == 'N':
        break
print(f"PyMp had {PyMp} votes")
print(f"IsMp had {IsMp} votes")
print(f"Total votes caste: {PyMp+IsMp}")
