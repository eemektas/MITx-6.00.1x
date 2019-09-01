word = 'bob'
count = 0
i = 0

while i + 2 <= len(s) - 1:
    if s[i] + s[i + 1] + s[i + 2] == 'bob':
        count += 1
    i += 1

print("Number of times bob occurs is:", count)