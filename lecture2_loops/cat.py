while True:
    n = int(input("What's n?"))
    if n > 10:
        continue
    elif n > 0:
        break

for _ in range(n):
    print("Meow")