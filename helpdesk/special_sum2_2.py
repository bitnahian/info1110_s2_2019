a = [7, 7, 3, 4, 7]

i = 0
to_skip = []

while i < len(a):
    if a[i] == 7:
        to_skip.append(i)
        if i+1 < len(a):
            to_skip.append(i+1)
    i += 1

i = 0
while i < len(to_skip):
    to_skip_index = to_skip[i]
    a[to_skip_index] = 0
    i+=1

print(sum(a))
