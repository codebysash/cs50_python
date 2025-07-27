def main():
    try:
        x = int(input("What is x?: "))
    except ValueError:
        print("Please enter valid number.")
        return

    if is_even(x):
        print("The number you have chosen is Even.")
    else:
        print("The number you have chosen is Odd.")

def is_even(n):
    return True if n % 2 == 0 else False

main()