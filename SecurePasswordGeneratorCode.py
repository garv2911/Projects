import secrets
import string

def generate_secure_password(length=16):
    """Generate a secure password."""

    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")
    
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least  one of each character
    all_chars = uppercase + lowercase + digits + symbols
    password = (
        secrets.choice(uppercase) +
        secrets.choice(lowercase) +
        secrets.choice(digits) +
        secrets.choice(symbols) +
        ''.join(secrets.choice(all_chars) for _ in range(length - 4))
    )
    password = ''.join(secrets.choice(password) for _ in range(length)) # Shuffle

    return password

# Generate and print secure password
print("generated secure password:", generate_secure_password)

