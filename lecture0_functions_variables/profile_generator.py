name = input("What's your full name? ").strip().title()
age = int(input("How old are you? "))
hobby = input("What's your favorite hobby? ")
current_year = 2025
birth_year = current_year - age
print("\n=== Personal Profile ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Born in: {birth_year}")
print(f"Favorite hobby: {hobby}")
print(f"Fun fact: {name}'s favorite hobby is {hobby} and is {age} years old which means the birth year is {birth_year}")
