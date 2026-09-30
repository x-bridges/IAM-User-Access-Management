IAM User Access Management System
Overview
This project is a beginner Identity and Access Management (IAM) system built with Python.
The system demonstrates basic IAM concepts including:
User account management
Role-Based Access Control (RBAC)
Permission management
Account activation and deactivation
User provisioning
User deprovisioning
Least privilege
Access control
Audit logging
The project uses CSV files to store users and roles and a text file to record account management activity.
Technologies Used
Python 
CSV
File handling
Command-line interface
Git/GitHub
Project Structure
IAM-User-Access-Management/
│
 iam.py
├── users.csv
├── roles.csv
├── access_log.txt
└── README.md

iam.py
The main Python program that manages users, roles, permissions, and account status.
users.csv
Stores user information including:
Username
Department
Role
Account status
roles.csv
Defines the permissions associated with each role.
Example:
Role
Permissions
Admin=
read/write/delete
Help Desk=
read/write
Employee=
read

access_log.txt
Records important account management actions with timestamps.
Examples include:
Account creation
Account disabling
Account enabling
Role changes
IAM Concepts Demonstrated
Role-Based Access Control
Users receive permissions based on their assigned role.
For example:
Admin → read, write, delete
Help Desk → read, write
Employee → read
This prevents every user from automatically receiving administrator-level permissions.
Least Privilege
Users are given only the permissions associated with their role.
For example, an Employee cannot perform administrative delete operations.
Account Deprovisioning
The system can disable a user's account.
A disabled account is denied access even if the user still has a role assigned.
Account Provisioning
The system can create new users and assign them a department and role.
Audit Logging
Important account changes are written to access_log.txt with timestamps.
This provides a basic audit trail for account management activity.
Features
View Users
Displays all users, their departments, roles, and account status.
Check Access
Checks whether a user has an active account and displays their assigned permissions.
Disable User
Changes a user's status to Disabled and records the action in the audit log.
Enable User
Changes a user's status back to Active and records the action in the audit log.
Change User Role
Allows a user's role to be changed while validating that the new role exists.
Create User
Creates a new user and assigns a valid role.
Check Specific Permission
Checks whether a specific user has a requested permission.
Example:
ACCESS GRANTED
xavier can delete

or:
ACCESS DENIED
craig cannot delete

How to Run
Make sure Python 3 is installed.
Check your Python version:
python3 --version

Navigate to the project directory:
cd ~/IAM-User-Access-Management

Run the program:
python3 iam.py

The program will display an interactive menu:
IAM USER MANAGEMENT

1. View users
2. Check access
3. Disable user
4. Enable user
5. Change user role
6. Create user
7. Check specific permission
8. Exit

Example
A user assigned the Admin role:
User: xavier
Role: Admin
Permissions: read/write/delete

A disabled user:
Access Denied - Account Disabled

A user without the requested permission:
ACCESS DENIED
craig cannot delete

Security Concepts
This project demonstrates several foundational cybersecurity concepts:
Identity management
Access control
RBAC
Least privilege
Account lifecycle management
User provisioning
User deprovisioning
Authorization
Audit logging
Future Improvements
Potential improvements include:
Password authentication
Password hashing
Multi-factor authentication
Database storage
Web interface
More detailed audit logs
Login attempt tracking
Automatic inactive-account detection
Integration with cloud IAM platforms


