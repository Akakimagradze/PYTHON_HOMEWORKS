i = 1

while i < 10:
    j = 1
    while j < i + 1:
        print(f"{j} * {i} = {j * i}", end="    ")
        j = j + 1
    print()
    i += 1

