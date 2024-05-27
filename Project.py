# Mini-Project: Contact Management System

import re
import json

# Initialize an empty dictionary to store contacts
contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    # Get contact details from the user
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information: ")

    # Store the contact in the dictionary
    contacts[phone] = {
        "name": name,
        "email": email,
        "additional_info": additional_info
    }
    print(f"Contact '{name}' added successfully!")

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone in contacts:
        print(f"Editing contact with phone number: {phone}")
        name = input("Enter updated name: ")
        email = input("Enter updated email address: ")
        additional_info = input("Enter updated additional information: ")

        # Update the contact
        contacts[phone]["name"] = name
        contacts[phone]["email"] = email
        contacts[phone]["additional_info"] = additional_info
        print(f"Contact with phone number {phone} updated successfully!")
    else:
        print(f"Contact with phone number {phone} not found.")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        contact_name = contacts[phone]["name"]
        del contacts[phone]
        print(f"Contact '{contact_name}' with phone number {phone} deleted successfully!")
    else:
        print(f"Contact with phone number {phone} not found.")

def search_contact():
    phone = input("Enter the phone number of the contact to search: ")
    if phone in contacts:
        print(f"Contact details for phone number {phone}:")
        print(f"Name: {contacts[phone]['name']}")
        print(f"Email: {contacts[phone]['email']}")
        print(f"Additional Info: {contacts[phone]['additional_info']}")
    else:
        print(f"Contact with phone number {phone} not found.")

def display_all_contacts():
    print("All Contacts:")
    for phone, contact in contacts.items():
        print(f"{phone}: {contact['name']}")

def export_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print(f"Contacts exported to {filename} successfully!")

def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
            print(f"Contacts imported from {filename} successfully!")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def quit_system():
    print("Exiting the Contact Management System. Goodbye!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_contacts("contacts.txt")
        elif choice == "7":
            import_contacts("imported_contacts.txt")
        elif choice == "8":
            quit_system()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

