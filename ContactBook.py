contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added!\n")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"\nName  : {name}")
        print(f"Phone : {contacts[name]['phone']}")
        print(f"Email : {contacts[name]['email']}\n")
    else:
        print("Contact not found!\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!\n")
    else:
        print("Contact not found!\n")

def view_all():
    if not contacts:
        print("No contacts yet!\n")
        return
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"{name} | {info['phone']} | {info['email']}")
    print()

print("=== Contact Book ===\n")
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    choice = input("\nChoose option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!\n")