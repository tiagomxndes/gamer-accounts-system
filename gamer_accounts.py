"""
Gamer Accounts System - Core Functionality

This program is designed to manage player accounts for an online gaming platform.
It reads account data from a file, allows the user to perform various operations,
and saves any changes back to the file.

The account data is stored in a text file ("college.txt") using CSV format:
- ID, Paid, Days, Status

Each field represents:
- ID : Player identifier starting with "PRO" (Pro players) or "CAS" (Casual players)
- Paid: Membership status ("Yes" or "No")
- Days: Number of days since last password reset (integer)
- Status: Account status ("Active", "Locked", "Disabled")

When the program starts, the file is read and the data is stored into four separate lists:
- players_id, pay_status, days and status
These lists are used throughout the program to manage and update account information.

The program provides a menu with the following options:

Option 1 - View All Accounts
Displays all account records in a formatted layout.
Shows membership status using symbols (✅ / ❎),
identifies player type (Pro or Casual), and highlights accounts that have not reset their password in over 90 days with an alert (🚨).

Option 2 - Delete a Record
Allows the user to remove an account by entering its ID.
If the ID exists, the record is deleted from all lists.
If not, an appropriate message is displayed.

Option 3 - Add a New Record
Allows the user to create a new account by entering a unique ID.
If the ID does not already exist, it is added with default values:
Paid = "No", Days = 0, Status = "Active".

Option 4 - Status
Allows the user to update the status of an existing account.
The user enters an ID and provides a new status value.

Option 5 - Waiting for instructions.

Option 6 - Waiting for instructions.

Option 7 - Waiting for instructions.

Option 8 - Quit and save
Saves all current data back to the file in CSV format and exists the program.

Additional Notes:
- The program does not use dictionaries or the CSV module, as per assignment requirements.
- Only Python concepts covered in class are used.
- All code included has been reviewed and understood.
"""


def read_accounts(filename):
    """
    Reads account data from a file and stores into four lists.

    :param filename: The name of the file containing account data.
    :return: Four lists containing account data:
        players_id: List of player IDs
        pay_status: List of payment statuses ("Yes" or "No").
        days: List of days since last password reset.
        status: List of account statuses ("Active", "Locked", "Disabled")

    """
    # Create the 4 empty lists
    players_id = []
    pay_status = []
    days = []
    status = []

    # Open the file and read each line
    with open(filename) as file:
        for line in file:

            # Remove spaces/newlines and split by comma
            line_parts = line.strip().split(",")

            # Store each value into its respective list
            players_id.append(line_parts[0])
            pay_status.append(line_parts[1])
            days.append(int(line_parts[2]))  # convert days to integer
            status.append(line_parts[3])

    # Return all lists
    return players_id, pay_status, days, status

def view_all_accounts(players_id, pay_status, days, status):
    """
    Displays all account details in a formatted output.

    Receives four lists containing account data and prints each account
    with additional formatting for readability.

    :param players_id: List of player IDs
    :param pay_status: List of payment statuses ("Yes" or "No")
    :param days: List of days since last password reset
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Output formatting:
        - Displays player type (Pro or Casual) based on ID prefix
        - Shows payment status using symbols (✅ / ❎)
        - Adds alert icon (🚨) if days > 90
    """

    # Loop through all accounts
    for i in range(len(players_id)):

        # Determine player type based on ID
        if players_id[i].startswith("PRO"):
            player_type = "Pro"
        else:
            player_type = "Casual"

        # Display payment status as symbol
        if pay_status[i] == "Yes":
            pay_symbol = "✅"
        else:
            pay_symbol = "❎"

        # Add alert icon if days > 90
        alert_icon = ""
        if days[i] > 90:
            alert_icon = "🚨"

        # Print formatted account information
        print(players_id[i], player_type, pay_symbol, status[i], alert_icon)

#Option 2
# Function to delete an account record by ID.
# Receives the 4 lists of account data.
# Prompts the user to enter an ID to delete.
# Checks if the ID exists in the players_id list:
#   If not found -> prints "ID not found".
#   If found -> removes the ID and all related data from all 4 lists.
# Prints a success message after the deletion is completed.

def del_account(players_id, pay_status, days, status):

    # Ask user for his ID
    user_id = input("What's your ID? ")

    #Check if user's ID exists in the list
    if user_id in players_id:
        index =  players_id.index(user_id)

        #Delete the record from all 4 lists
        del players_id[index]
        del pay_status[index]
        del days[index]
        del status[index]

        #Prints success message after the deletion is completed
        print(f"Account {user_id} has been deleted successfully.")

    else:
        #Prints error message if ID not found
        print("ID not found.")

#Option 3
# Function to add a new account record.
# Receives the 4 lists of account data.
# Prompts the user to enter a new ID.
# Checks if the ID already exists in the players_id list:
#   If it exists, prints an error message.
#   If it doesn't exist, it adds the new ID to the list.
# Adds default values to the other lists:
#   Paid = "No", Days = 0, Status = "Active".
# Prints a success message after the account is added.

def add_account(players_id, pay_status, days, status):

    #Ask user for his ID
    new_id = input("Enter new ID: ")

    #Check if the ID already exists
    if new_id in players_id:
        print("Error, the ID entered already exists.")

    else:
        #Add new record with the default values
        players_id.append(new_id)
        pay_status.append("No")
        days.append(0)
        status.append("Active")

        #Print success message after new ID added
        print(f"Account {new_id} was added successfully")

# Function 4
# Function to update the status of an account
# Received the players_id and status lists
# Prompts the user to enter an ID
# Checks if the ID exists in the players_id list
#   If ID not found, print "ID not found"
#   If ID found, asks for a new status and updates the status list
# Prints a success message after the update is completed

def update_status(players_id, status):
    user_id = input("Enter your ID: ")

    #Check if the ID exists
    if user_id in players_id:
        index=players_id.index(user_id)

        #Ask user for new status
        new_status = input("Enter your new status (Active/Locked/Disabled): ")
        status[index]=new_status

        #Print success message
        print(f"Status for {user_id} has been successfully updated.")

        #Print ID not found
    else:
        print("ID not found.")

# Option 8
# Function to save all account data to file and exit the program.
# Receives the 4 lists of account data.
# Writes all data back to "college.txt" in CSV format.
# Each record is written in the format: ID, Paid, Days, Status.
# Exits the program after saving is completed

def save_and_quit(filename, players_id, pay_status, days, status):

    #Open file in W mode (overwrites existing data)
    with open(filename, "w") as file:
        for i in range(len(players_id)):
            line = players_id[i] + "," + pay_status[i] + "," + str(days[i]) + "," + status[i]
            file.write(line + "\n")

    print("Data saved successfully. Exiting program now.")

#Testing my code

# Load account data from college.txt to test functionality
players_id, pay_status, days, status = read_accounts("college.txt")

# Call the add_account function to test adding a new record
add_account(players_id, pay_status, days, status)

#Print all the accounts to verify if the new record was added correctly
for i in range(len(players_id)):
    print(players_id[i], pay_status[i], days[i], status[i])

#Test update function
update_status(players_id, status)

#Print to verify change
view_all_accounts(players_id, pay_status, days, status)

# Test save function to write changes back to the file
save_and_quit("college.txt", players_id, pay_status, days, status)