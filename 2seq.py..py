user = input('enter your numbers, divide by coma: ')
counts = user.split(',')
result = []
for user in counts:
    if counts.count(user) == 1:
        result.append(user)
print(result)

