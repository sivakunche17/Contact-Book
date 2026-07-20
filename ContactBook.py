
#9th mini project
#Contact Book

contacts = {}

while True:
    print("\n-=-=-= Contact Book =-=-=-")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("-__-__-__-__-__-__-__-__-__-")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        Name = input("Enter your name: ")
        Phone = input("Enter your ph.no: ")
        contacts[Name] = Phone
        print("Contacted Added Successfully")
    elif choice == "2":
        for Name, Phone in contacts.items():
            print("Name:", Name)
            print("Phone:", Phone)
    elif choice == "3":
        Search = input("Enter Name to Search: ")
        if Search in contacts:
            print("Name:", Search)
            print("Phone:", contacts[Search])
        else:
            print("Contact Not found")
    elif choice == "4":
        old_name = input("Search name to update: ")

        if old_name in contacts:
            new_name = input("Enter your new name to update:")
            new_phone = input("Enter new ph.no to update: ")
            contacts.pop(old_name)
            contacts[new_name] = new_phone

            print("contact updated succesfully")

        else:
            print("contact not found")

    elif choice == "5":
        delete_name = input("Search contact name to delete: ")
        if delete_name in contacts:
            contacts.pop(delete_name)
            print("Contact Delete Successfully")
        else:
            print("contact not found")
    elif choice == "6":
        print("Contact Book Closed")
        break
    else:
        print("invalid choice")