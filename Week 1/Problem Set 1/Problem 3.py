temp = ''
sub = ''

for i in range(len(s)):
    if temp == '':
        temp = s[i]
    elif temp[-1] <= s[i]:
        temp += s[i]
    elif temp[-1] > s[i]:
        if len(temp) > len(sub):
            sub = temp
        temp = s[i]

if len(temp) > len(sub):
    sub = temp

print(sub)