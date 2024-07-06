"""
### Assignment: Password Manager Program

#### Objective:
Create a password manager program that allows users to store, retrieve, and manage their passwords. 
The program will use file handling to save and read data, and it will be run in the terminal.

#### Requirements:
1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
3. **Basic Operations**:
    - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
    - **Retrieve a password**: Ask for the website and return the username and password.
    - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

#### Program Flow:
1. Display a menu with the following options:
    - Add a new password
    - Retrieve a password
    - Delete a password
    - Exit
2. Based on the user's choice, perform the corresponding operation.
3. Repeat the menu until the user chooses to exit.

#### Detailed Instructions:
1. **Menu Display**: Create a function to display the menu and get the user's choice.
2. **Add Password**:
    - Prompt the user for the website, username, and password.
    - Write this information to a file in a structured format.
3. **Retrieve Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Display the username and password.
4. **Delete Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Remove the entry and update the file.
5. **File Format**: Store each entry in a new line in the format:
    ```
    website,username,password
    ```

#### Example:
1. **Add Password**:
    ```
    Enter website: example.com
    Enter username: user1
    Enter password: pass123
    Password saved successfully!
    ```
2. **Retrieve Password**:
    ```
    Enter website: example.com
    Username: user1
    Password: pass123
    ```
3. **Delete Password**:
    ```
    Enter website: example.com
    Password deleted successfully!
    ```

#### Hints:
- Use functions to keep your code organized.
- Use lists and dictionaries to manage the data in memory before writing to or reading from the file.
- Ensure to handle cases where the file may not exist initially.

#### Additional Notes:
- Focus on functionality rather than security for this assignment.
"""

"""
create the same program again but this time file data should be stored in json
"""

"""
create the same program again but this time file data should be stored in binary using pickle module
"""

import inquirer
import os
import sys
import json

def add_password():
    try:
        questions = [
            inquirer.Text(
                'website',
                message="Enter website",
                default='',
            ),
            inquirer.Text(
                'username',
                message="Enter username",
                default='',
            ),
            inquirer.Password(
                'password',
                message="Enter password",
                default='',
            ),
        ]
        
        answers = inquirer.prompt(questions)
        
        data = []
        
        a_file = open('passwords.json', 'a')
        r_file = open('passwords.json')
        next_data = r_file.read()
        r_file.close()
        print("Next Data ===>", next_data)
        data = json.loads(next_data or '[]')
        print("Data ===>", data)
        data.append(answers)
        print("Data 2 ===>", data)
        data = json.dumps(data, indent=4)
        print("Data 3 ===>", data)
        a_file.truncate(0)
        print("Data 4 ===>", data)
        a_file.write(data)
        print("Data 5 ===>", data)
        print("Info saved successfully!")
        a_file.close()
        # with open('passwords.json', 'r+') as file:
        #     data = json.loads(file.read() or '[]')
        #     data.append(answers)
        #     data = json.dumps(data, indent=4)
        #     file.close()
        
        # with open('passwords.json', '+w') as file:
        #     file.write(data)
        #     print("Info saved successfully!")
        #     file.close()
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        input("Press enter to continue")
        homepage()

def retrieve_password():
    try:
        questions = [
            inquirer.Text(
                'website',
                message="Enter website",
                default='',
            ),
        ]
        
        answers = inquirer.prompt(questions)
        isExist = False

        with open('passwords.json', 'r+') as file:
            data = json.loads(file.read() or '[]')
            
            for item in data:
                website = item["website"]
                username = item["username"]
                password = item["password"]

                if website == answers['website']:
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    isExist = True
                    return
                line = file.readline()
            file.close()
        if isExist == False:
            print("No password found for this website!")
    except FileNotFoundError as e:
        print("Please add some records first")
    except EOFError as e:
        file.close()
        print("No password found for this website!")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        input("Press enter to continue")
        homepage()

def delete_password():
    try:
        questions = [
            inquirer.Text(
                'website',
                message="Enter website",
                default='',
            ),
        ]
        
        answers = inquirer.prompt(questions)
        
        lines = []

        data = []
        
        with open('passwords.json', 'r') as file:
            data = json.loads(file.read() or '[]')
            file.close()

        with open('passwords.json', 'w+') as file:
            for (i, item) in enumerate(data):
                if item['website'] == answers['website']:
                    del data[i]
                    file.write(json.dumps(data, indent = 4))
                    file.close()
                    print("Password deleted successfully!")
                    return
            file.write(json.dumps(data, indent = 4))
            file.close()
        print("Website not found")
    except FileNotFoundError as e:
        print("Please add some records first")
    except EOFError as e:
        file.close()
        print("No password found for this website!")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        input("Press enter to continue")
        homepage()

def homepage():
    os.system('cls||clear')

    questions = [
        inquirer.List(
            'menu',
            message="Menu",
            choices=[
                ('1. Add a new password', 1),
                ('2. Retrieve a password', 2),
                ('3. Delete a password', 3),
                ('4. Exit', 4),
            ],
            default=[5]
        ),
    ]

    choice = inquirer.prompt(questions)

    if choice != None:
        choice = choice['menu']

    if choice == 1:
        add_password()
    elif choice == 2:
        retrieve_password()
    elif choice == 3:
        delete_password()
    elif choice == 4:
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice!")
        input("Press enter to continue")
        homepage()

homepage()