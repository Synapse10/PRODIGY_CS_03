import re

def assess_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

def main():
    password = input("Enter a password: ")
    strength = assess_password_strength(password)

    print(f"The password '{password}' is {strength}.")

    if strength == "Weak":
        print("The password is weak. It should be at least 12 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters.")
    elif strength == "Medium":
        print("The password is medium. It's a good start, but consider adding more characters or a mix of character types to make it stronger.")

if __name__ == "__main__":
    main()