# Ask the user to enter a password
password = input("Enter your password: ")

# Set up conditions
has_upper = False
has_lower = False
has_number = False
has_special = False
special_characters = "!@#$%^&*()-_+=<>?/"

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True
    elif char in special_characters:
        has_special = True

# Count how many types are present
score = 0
if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_number:
    score += 1
if has_special:
    score += 1

# Give feedback
if score == 5:
    print("Your password is Strong!")
elif score >= 3:
    print("Your password is Moderate")
else:
    print("Your password is Weak make a strong password")










