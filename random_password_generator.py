import random
import string

def generate_password(length, include_special_chars):
    characters = string.ascii_letters + string.digits

    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k= length))

    return password

# Main function to run the program

def main():
    length = int(input("Enter Password Length: "))

    include_special_chars = input("Do you want to include special character? (y/n):").lower() == "y"

    password = generate_password(length, include_special_chars)

    print(f"Your password is: {password}")

if __name__ == "__main__" :
    main()

