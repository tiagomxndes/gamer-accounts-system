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

# ===========================
# LOAD  DATA FUNCTION
# ===========================
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

# ===========================
# OPTION 1 - VIEW ACCOUNTS
# ===========================
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

        # Determine player type based on ID (case-insensitive)
        if players_id[i].upper().startswith("PRO"):
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
        print(f"{players_id[i]:10} {player_type:8} {pay_symbol:4} {status[i]:10} {alert_icon}")

# ==========================
# OPTION 2 - DELETE ACCOUNT
# ===========================
def del_account(players_id, pay_status, days, status):
    """
    Deletes an account from the system based on user ID.

    Receives four lists containing account data and removes the matching
    record from all lists if the ID exists.

    :param players_id: List of player IDs
    :param pay_status: List of payment statuses ("Yes" or "No")
    :param days: List of days since last password reset
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Process:
        - Prompts the user to enter an ID
        - Checks if the ID exists in the players_id lists
        - If found, deletes the record from all four lists
        - If not found, displays an error message
    """

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

# ===========================
# OPTION 3 - LOAD ACCOUNT
# ===========================
def add_account(players_id, pay_status, days, status):
    """
    Adds a new account to the system if the ID doesn't already exist.

    Receives four lists containing account data and  allows the user to create
    a new account with default values.

    :param players_id: List of player IDs
    :param pay_status: List of payment Statuses("Yes" or "No")
    :param days: List of days since last password reset
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Process:
        - Prompts the user to enter a new ID
        - Checks if the ID already exists in the players_id list
        - If it exists, displays an error message
        - If it doesn't exist, adds the ID with default values such as:
            Paid = "No", Days = 0, Status = "Active"
        - Displays a success message after adding the account
    """

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

# ===========================
# OPTION 4 - UPDATE STATUS
# ===========================
def update_status(players_id, status):
    """
    Updates the status of an existing account.
    Receives the two lists containing account data and allows the user to update
    the status of a specific account.

    :param players_id: List of player IDs
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Process:
        - Prompts the user to enter an ID
        - Checks if the ID exists in the players_id list
        - If ID found, ask for a new status and updates it
        - If ID not found, displays "ID not found"
        - Displays a success message after updating the status
    """

    user_id = input("Enter your ID: ")

    #Check if the ID exists
    if user_id in players_id:
        index=players_id.index(user_id)

        #Ask user for new status
        new_status = input("Enter your new status (Active/Locked/Disabled): ")

        # Validate status input
        if new_status not in ["Active", "Locked", "Disabled"]:
            print("Invalid status")
            return

        status[index]=new_status

        #Print success message
        print(f"Status for {user_id} has been successfully updated.")

    #Print ID not found
    else:
        print("ID not found.")
# ===========================
# OPTION 5 - PLAYER TYPE PERCENTAGES
# ===========================
def player_type_percentages(players_id):
    """
    Calculates and displays the percentage of casual and professional gamers.

    Receives the list of players IDs and determines how many players belong to each category
    (Pro or Casual) and then converts these counts into percentages of the total number of players.

    :param players_id: List of player IDs
    :return: None

    Process:
        - Counts how many IDs start with "PRO"
        - Counts how many IDs start with "CAS"
        - Calculates the percentage of each type based on total players.
        - Prints the results in a clear format
    """

    total_players = len(players_id)

    if total_players == 0:
        print("No players in the system.")

    pro_players_count = 0
    casual_players_count = 0

    #Count player types
    for players_id in players_id:
        if players_id.upper().startswith("PRO"):
            pro_players_count += 1
        else:
            casual_players_count += 1

    #Calculate the percentages
    pro_players_percentage = (pro_players_count/total_players) * 100
    casual_players_percentage = (casual_players_count / total_players) * 100

    #Print the results neatly
    print("========= PLAYER TYPE PERCENTAGES =========")
    print(f"Professional players: {pro_players_percentage:.2f}%")
    print(f"Casual players: {casual_players_percentage:.2f}%")
    print("===========================================")

# ===========================
# OPTION 6 - EXPORT ACCOUNTS BY STATUS
# ===========================
def export_players_by_status(players_id, status):
    """
    Exports player IDs into separate files based on their account status.

    Receives the list of player IDs and their corresponding account statuses, then
    writes each ID into a specific file depending on whether the account is
    Active, Locked or Disabled.

    :param players_id: List of Player IDs
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Process:
        - Opens the three files separately : active.txt, locked.txt, disabled.txt
        - Iterates through all players
        - Writes each player ID into the corresponding file based on status.
        - Close all the files after writing
        - Displays a confirmation message.
    """

    #Open all the files separately
    active_file = open("active.txt", "w")
    locked_file = open("locked.txt", "w")
    disabled_file = open("disabled.txt", "w")

    #Go through all players
    for i in range(len(players_id)):

        if status[i] == "Active":
            active_file.write(players_id[i] + "\n")

        elif status[i] == "Locked":
            locked_file.write(players_id[i] + "\n")

        elif status[i] == "Disabled":
            disabled_file.write(players_id[i] + "\n")

    #Close all the files
    active_file.close()
    locked_file.close()
    disabled_file.close()

    print("All the accounts were successfully exported by status.")

# ===========================
# OPTION - 7 DISABLE UNPAID ACCOUNTS
# ===========================
def disable_unpaid_account(pay_status, status):

    updated_count = 0

    #Go through all accounts
    for i in range(len(pay_status)):

        #Check the conditions
        if pay_status[i] == "No" and status[i] == "Active":
            status[i] = "Disabled"
            updated_count += 1

    return updated_count

# ===========================
# OPTION - 8 SAVE AND QUIT
# ===========================
def save_and_quit(filename, players_id, pay_status, days, status):
    """
    Saves all account data back to a file in CSV format and exits the program.

    Receives four lists containing account data and writes them back to the
    specified file, overwriting his existing content.

    :param filename: The name of the file to save data to
    :param players_id: List of player IDs
    :param pay_status: List of payment statuses ("Yes" or "No")
    :param days: List of fays since last password reset
    :param status: List of account statuses ("Active", "Locked", "Disabled")
    :return: None

    Process:
        - Opens the file in write mode (overwrites existing data)
        - Writes each account in CSV format: ID, Paid, Days, Status
        - Saves all records to the file
        - Displays a confirmation message before exiting
    """

    #Open file in W mode (overwrites existing data)
    with open(filename, "w") as file:
        for i in range(len(players_id)):
            line = players_id[i] + "," + pay_status[i] + "," + str(days[i]) + "," + status[i]
            file.write(line + "\n")

    print("Data saved successfully. Exiting program now.")

# ===========================
# MAIN MENU SYSTEM
# ===========================

def main():

    players_id, pay_status, days, status = read_accounts("college.txt")

    while True:
        print("========== GAMER ACCOUNTS SYSTEM ==========")
        print("1. View all accounts")
        print("2. Delete account")
        print("3. Add account")
        print("4. Update status")
        print("5. Player type percentages")
        print("6. Export account by status")
        print("7. Disable unpaid accounts")
        print("8. Save and quit")
        print("===========================================")

        # Handles invalid input for menu selection to prevent crashes when a non-numeric value is entered
        try:
            user_choice = int(input("Please, select an option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if user_choice == 1:
            view_all_accounts(players_id, pay_status, days, status)

        elif user_choice == 2:
            del_account(players_id, pay_status, days, status)

        elif user_choice == 3:
            add_account(players_id, pay_status, days, status)

        elif user_choice == 4:
            update_status(players_id, status)

        elif user_choice == 5:
            player_type_percentages(players_id)

        elif user_choice == 6:
            export_players_by_status(players_id, status)

        elif user_choice == 7:
            updated_records = disable_unpaid_account(pay_status, status)
            print(f"{updated_records} accounts were disabled due to non-payment.")

        elif user_choice == 8:
            save_and_quit("college.txt", players_id, pay_status, days, status)
            break

        else:
            print("Invalid option, please try again.")

# ===========================
# PROGRAM START
# ===========================

if __name__ == '__main__':
    main()