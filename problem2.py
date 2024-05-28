# Write a program to check char is vowel or not.

vowels = ['a','e','i','o','u']

character = input("Enter a character: ")[0]

if character.lower() in vowels:
    print(f""""{character}" is a vowel""")
else: 
    print(f""""{character}" is a consonant""")