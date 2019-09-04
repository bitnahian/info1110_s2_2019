num = 1
line = ''

while num < 100:
    if num % 2 == 1:
        if num == 99:
            line += str(num)
            break
        line += str(num) + ', '

    num += 1

print(line)
