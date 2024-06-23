import bcrypt

# Plain text passwords
passwords = {
    "dp": "Sweet_Rug",
    "ohm": "Sweet_Rug"
}

# Dictionary to store hashed passwords
hashed_passwords = {}

for username, password in passwords.items():
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed = bcrypt.hashpw(password.encode(), salt)
    # Store the hashed password
    hashed_passwords[username] = hashed.decode()

# Print the hashed passwords
for username, hashed_password in hashed_passwords.items():
    print(f"{username}: {hashed_password}")