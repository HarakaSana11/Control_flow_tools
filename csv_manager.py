#!/usr/bin/python3
import csv
import os

# Define the path to the CSV file
csv_file = 'users.csv'

# Function to create or read from the CSV file
def create_or_read_csv():
    if not file_exists(csv_file):
        create_csv()
    else:
        filter_inactive_users()

# Function to check if the CSV file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Function to create a new CSV file
def create_csv():
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Status"])
        writer.writeheader()
    print(f"CSV file '{csv_file}' created successfully.")

# Function to read data from an existing CSV file
def read_csv():
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to update the CSV file with the user's data
def update_csv(name, email, status):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Status"])
        writer.writerow({"Name": name, "Email": email, "Status": status})
    print("Thank you! Your information has been recorded.")

# Function to filter out inactive users from the CSV file
def filter_inactive_users():
    active_users = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for user in reader:
            if user['Status'].lower() == 'active':
                active_users.append(user)
    print("Active Users:")
    print_csv(active_users)

# Function to print CSV-formatted data
def print_csv(data):
    if not data:
        print("No active users found.")
        return
    headers = data[0].keys()
    print(','.join(headers))
    for row in data:
        values = [row[header] for header in headers]
        print(','.join(values))

# Main function
def main():
    create_or_read_csv()

if __name__ == "__main__":
    main()


