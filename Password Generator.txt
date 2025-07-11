import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password has at least one letter, digit, and punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length
    password += random.choices(characters, k=length - 4)

    # Shuffle the list to avoid predictable pattern
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# -------- Main Program --------
try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
