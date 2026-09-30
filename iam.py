import csv
from datetime import datetime


def get_valid_roles():
    roles = []

    with open("roles.csv", "r") as file:
        reader = csv.DictReader(file)

        for role in reader:
            roles.append(role["role"])

    return roles


def view_users():
    with open("users.csv", "r") as file:
        users = csv.DictReader(file)

        for user in users:
            print(
                user["username"],
                "|",
                user["department"],
                "|",
                user["role"],
                "|",
                user["status"]
            )


def check_access(username):
    with open("users.csv", "r") as file:
        users = csv.DictReader(file)

        for user in users:

            if user["username"] == username:

                if user["status"] == "Disabled":
                    print("Access Denied - Account Disabled")
                    return

                with open("roles.csv", "r") as role_file:
                    roles = csv.DictReader(role_file)

                    for role in roles:

                        if role["role"] == user["role"]:
                            print("User:", username)
                            print("Role:", user["role"])
                            print("Permissions:", role["permissions"])
                            return

                print("Role not found.")
                return

        print("User not found.")


def check_permission(username, requested_permission):

    valid_permissions = [
        "read",
        "write",
        "delete"
    ]

    if requested_permission not in valid_permissions:

        print("Invalid permission.")
        print("Available permissions: read, write, delete")

        return

    with open("users.csv", "r") as file:
        users = csv.DictReader(file)

        for user in users:

            if user["username"] == username:

                if user["status"] == "Disabled":

                    print("ACCESS DENIED")
                    print("Reason: Account is disabled.")

                    return

                with open("roles.csv", "r") as role_file:
                    roles = csv.DictReader(role_file)

                    for role in roles:

                        if role["role"] == user["role"]:

                            permissions = role["permissions"].split("/")

                            if requested_permission in permissions:

                                print("ACCESS GRANTED")
                                print(
                                    username,
                                    "can",
                                    requested_permission
                                )

                            else:

                                print("ACCESS DENIED")
                                print(
                                    username,
                                    "cannot",
                                    requested_permission
                                )

                            return

                print("Role not found.")
                return

        print("User not found.")


def disable_user(username):

    users = []
    found = False

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)

        for user in reader:

            if user["username"] == username:

                user["status"] = "Disabled"
                found = True

            users.append(user)

    if not found:

        print("User not found.")

        return

    with open("users.csv", "w", newline="") as file:

        fieldnames = [
            "username",
            "department",
            "role",
            "status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(users)

    with open("access_log.txt", "a") as log:

        log.write(
            f"{datetime.now()} - "
            f"Disabled account: {username}\n"
        )

    print(username, "has been disabled.")


def enable_user(username):

    users = []
    found = False

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)

        for user in reader:

            if user["username"] == username:

                user["status"] = "Active"
                found = True

            users.append(user)

    if not found:

        print("User not found.")

        return

    with open("users.csv", "w", newline="") as file:

        fieldnames = [
            "username",
            "department",
            "role",
            "status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(users)

    with open("access_log.txt", "a") as log:

        log.write(
            f"{datetime.now()} - "
            f"Enabled account: {username}\n"
        )

    print(username, "has been enabled.")


def change_role(username, new_role):

    valid_roles = get_valid_roles()

    if new_role not in valid_roles:

        print("Invalid role.")
        print("Available roles:")

        for role in valid_roles:

            print("-", role)

        return

    users = []
    found = False

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)

        for user in reader:

            if user["username"] == username:

                user["role"] = new_role
                found = True

            users.append(user)

    if not found:

        print("User not found.")

        return

    with open("users.csv", "w", newline="") as file:

        fieldnames = [
            "username",
            "department",
            "role",
            "status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(users)

    with open("access_log.txt", "a") as log:

        log.write(
            f"{datetime.now()} - "
            f"Changed {username} role to {new_role}\n"
        )

    print(
        username,
        "role changed to",
        new_role
    )


def create_user(username, department, role):

    valid_roles = get_valid_roles()

    if role not in valid_roles:

        print("Invalid role.")
        print("Available roles:")

        for valid_role in valid_roles:

            print("-", valid_role)

        return

    with open("users.csv", "r") as file:

        users = csv.DictReader(file)

        for user in users:

            if user["username"] == username:

                print("Username already exists.")

                return

    with open("users.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            username,
            department,
            role,
            "Active"
        ])

    with open("access_log.txt", "a") as log:

        log.write(
            f"{datetime.now()} - "
            f"Created user: {username} "
            f"with role: {role}\n"
        )

    print(
        username,
        "has been created."
    )


while True:

    print("\nIAM USER MANAGEMENT")
    print("1. View users")
    print("2. Check access")
    print("3. Disable user")
    print("4. Enable user")
    print("5. Change user role")
    print("6. Create user")
    print("7. Check specific permission")
    print("8. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        view_users()

    elif choice == "2":

        username = input(
            "Enter username: "
        )

        check_access(username)

    elif choice == "3":

        username = input(
            "Enter username: "
        )

        disable_user(username)

    elif choice == "4":

        username = input(
            "Enter username: "
        )

        enable_user(username)

    elif choice == "5":

        username = input(
            "Enter username: "
        )

        new_role = input(
            "Enter new role: "
        )

        change_role(
            username,
            new_role
        )

    elif choice == "6":

        username = input(
            "Enter username: "
        )

        department = input(
            "Enter department: "
        )

        role = input(
            "Enter role: "
        )

        create_user(
            username,
            department,
            role
        )

    elif choice == "7":

        username = input(
            "Enter username: "
        )

        permission = input(
            "Enter permission "
            "(read/write/delete): "
        )

        check_permission(
            username,
            permission
        )

    elif choice == "8":

        print("Goodbye!")

        break

    else:

        print("Invalid option.")