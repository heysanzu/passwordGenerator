import random
import string

def generate_strong_password(length=16):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    all_chars = lowercase + uppercase + digits + special
    password += random.choices(all_chars, k=length - 4)
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Strong Password Generator\n")
    
    while True:
        try:
            length = input("Enter password length (minimum 8, recommended 16+): ")
            length = int(length)
            if length < 8:
                print("Password too short! Minimum length is 8 characters.\n")
                continue
            break
        except ValueError:
            print("Please enter a valid number.\n")
    
    password = generate_strong_password(length)
    
    print(f"\nYour strong password: {password}")
    print(f"Password length: {len(password)} characters")
    print("\nPassword includes:")
    print("✓ Lowercase letters")
    print("✓ Uppercase letters")
    print("✓ Numbers")
    print("✓ Special characters")
    
    while True:
        again = input("\nGenerate another password? (y/n): ").lower()
        if again == 'y':
            password = generate_strong_password(length)
            print(f"\nYour strong password: {password}")
        else:
            print("\nStay secure!")
            break

if __name__ == "__main__":
    main()
