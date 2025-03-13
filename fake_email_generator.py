import random
import string
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Use pyfiglet for large font text
ascii_banner = pyfiglet.figlet_format("cod4hack Fake Email Generator")

public email_domains; 

def  set_email_type():
    email_type = input("Enter the email type (e.g. gmail.com): ")
    email_domains= email_type

def generate_random_email(length=7):
    # Generate a random string of letters and digits
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    # Return the email address
    return f"{random_string}@{email_domains}"

def generate_emails(count):
    emails = []
    for _ in range(count):
        email = generate_random_email()
        emails.append(email)
    return emails

# Display log message in red with large font
print(Fore.RED + ascii_banner)

# Ask user to enter the number of emails to generate
try:
    number_of_emails = int(input("Enter the number of emails to generate: "))
    if number_of_emails <= 0:
        raise ValueError("Number of emails should be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    # Generate the requested number of emails
    set_email_type()
    email_list = generate_emails(number_of_emails)

    # Write the emails to a file
    with open('random_emails.txt', 'w') as file:
        for email in email_list:
            file.write(f"{email}\n")

    print(f"{number_of_emails} emails generated and saved to 'random_emails.txt'.")
