import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("You must select at least one character type!")

    # Ensure at least one character from each selected set
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password
    password += random.choices(character_pool, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator 🔐")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\n✅ Generated Password: {password}")

    except ValueError:
        print("❌ Invalid input. Please enter a positive integer and choose at least one character type.")

if __name__ == "__main__":
    main()
