#!/usr/bin/python3
import csv_manager

# Function to prompt the user for their full name and email
def prompt_user():
    while True:
        name = input("Please enter your full name (at least two names): ")
        if len(name.split()) < 2:
            print("Please provide at least two names.")
            continue
        email = input("Please enter your email address: ")
        if not is_valid_email(email):
            print("Please enter a valid email address.")
            continue
        return name, email

# Function to validate an email address
def is_valid_email(email):
    # This is a simple validation for demonstration purposes
    # In a real application, you should use a more comprehensive method
    return '@' in email

# Function to determine the user's activity status
def determine_activity():
    print("How often do you exercise?")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Rarely")
    print("5. Never")
    answer = input("Choose an option (1-5): ")
    if answer in ['1', '2', '3']:
        return 'active'
    else:
        return 'inactive'

# Main function
def main():
    # Prompt the user for details
    name, email = prompt_user()
    status = determine_activity()
    
    # Update the CSV file with the user's data
    csv_manager.update_csv(name, email, status)

if __name__ == "__main__":
    main()
