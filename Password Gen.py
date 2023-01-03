import secrets
import string

def generate_password(length):
  # Generate a random string of digits, uppercase letters, and lowercase letters
  password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
  return password

# Generate a random password of 10 characters
password = generate_password(10)
print(password)
