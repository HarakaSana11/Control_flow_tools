#!/usr/bin/python3
import csv
import os

# Define the path to the CSV file
csv_file = 'users.csv'

# Function to prompt the user for their full name and email
def prompt_user():
    name = input("Please enter your full name: ")
    email = input("Please enter your email address: ")
    return name, email

# Function to prompt the user with lifestyle questions to determine if they are active
def determine_activity():
    print("How often do you exercise?")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Rarely")
    print("5. Never")
    answer = input("Choose an option (1-5): ")
    if answer == '1':
        return 'active'
    elif answer in ['2', '3']:
        return 'active'
    else:
        return 'inactive'

# Function to update the CSV file with the user's data
def update_csv(name, email, status):
    if not user_or_email_exists(name, email):
        data = {'Name': name, 'Email': email, 'Status': status}
        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Status"])
            writer.writerow(data)
        print("Thank you! Your information has been recorded.")
    else:
        print("The name or email is already in our system. Thank you for confirming your status again.")

# Function to check if the CSV file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Function to check if the user or email already exists in the CSV file
def user_or_email_exists(name, email):
    if not file_exists(csv_file):
        return False
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'Name' in row and row['Name'].lower() == name.lower():
                return True
            if 'Email' in row and row['Email'].lower() == email.lower():
                return True
    return False

# Main function
def main():
    name, email = prompt_user()
    status = determine_activity()
    update_csv(name, email, status)

if __name__ == "__main__":
    main()
