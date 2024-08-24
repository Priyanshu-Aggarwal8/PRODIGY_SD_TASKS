#Task 3: Program that allows users to store and manage contact information
#I will use a JSON file to store contacts, so that they persist through different sessions

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email address: ").strip()

    if name in contacts:
        print(f"Contact with name {name} already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("\nNo contacts found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Delete a contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
