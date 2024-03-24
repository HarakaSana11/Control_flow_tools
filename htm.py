#!/usr/bin/python3
import os
import csv

# Define the path to the CSV file
csv_file = 'users.csv'

# Function to create or read from the CSV file
def create_or_read_csv():
    if not file_exists(csv_file):
        create_csv()
    else:
        active_users = filter_active_users()
        if active_users:
            delete_inactive_users()
        return active_users

# Function to check if the CSV file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Function to create a new CSV file
def create_csv():
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Status"])  # Customize fieldnames as needed
        writer.writeheader()
    print(f"CSV file '{csv_file}' created successfully.")

# Function to filter out active users
def filter_active_users():
    active_users = []
    if not file_exists(csv_file):
        return active_users
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, status = row
                if status.strip().lower() == 'active':
                    active_users.append({'Name': name.strip(), 'Status': status.strip().lower()})
    return active_users

# Function to delete inactive users from the CSV file
def delete_inactive_users():
    rows_to_keep = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, status = row
                if status.strip().lower() == 'active':
                    rows_to_keep.append(row)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows_to_keep:
            writer.writerow(row)

# Main function
def main():
    active_users = create_or_read_csv()
    if active_users:
        print("List of active users:")
        for user in active_users:
            print(user)

if __name__ == "__main__":
    main()
