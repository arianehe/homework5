records = [0] * 26

with open('book.txt', 'r') as file:
    content = file.read()
    for char in content:
        code = ord(char)
        if 97 <= code <= 122:
            records[code - 97] += 1
        elif 65 <= code <= 90:
            records[code - 65] += 1

with open('summary.txt', 'w') as file:
    sum = 0
    for i in range(len(records)):
        if records[i] > 0:
            file.write("{} {}\n".format(chr(i + 65), records[i]))
            sum += 1
    if sum == 26:
        file.write("\nIt has all letters.")
    else:
        file.write("\nIt doesn’t have all letters.")