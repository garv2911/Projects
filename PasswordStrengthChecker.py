import re

def check_password_strength(password):
    strength_score = 0

    # Criteria
    length_criteria = len(password) >= 8  # At least 8 characters
    lowercase_criteria = re.search(r'[a-z]', password)  # At least one lowercase letter
    uppercase_criteria = bool(re.search(r'[A-Z]',password)) # At least one uppercase
    digit_criteria = bool(re.search(r'\d',password)) # At least one number
    special_char_criteria = bool(re.search(r'[@#$%^&*?&]', password)) # At least one special character

    if length_criteria: strength_score +=1
    if lowercase_criteria: strength_score += 1
    if uppercase_criteria: strength_score += 1
    if digit_criteria: strength_score += 1
    if special_char_criteria: strength_score += 1

    if strength_score == 5:
        return "Strong (Great job)"
    elif strength_score >= 3:
        return "Medium (Consider making it stronger)"
    else:
        return  "Weak (Your password is too easy to guess)"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")