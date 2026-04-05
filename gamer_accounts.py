"""
Gamer Accounts System - Core Functionality

DATA:
- Stored in "college.txt" as CSV: ID, Paid, Days, Status
- ID: starts with "PRO" (Pro gamers) or "CAS" (Casual Players)
- Paid: "Yes" or "No"
- Days: integers, days since last password reset
- Status: "Active", "Locked", "Disabled"
- Read this file into 4 separate lists such as: ids, paid, days, status

MENU OPTIONS: 

Option 1 - VIEW ALL ACCOUNTS: (Write a function that receives all 4 lists, and displays the accounts in a formatted table.)

    - Display all accounts in a formatted table.
    - Show ✅ if Paid == "Yes", ❎ otherwise.
    - Append "Casual" for IDs starting with "CAS", "Pro" for "PRO".
    - Highlight accounts with days > 90 with 🚨.

Option 2 - DELETE A RECORD: (Write a function that receives all 4 lists.)

    - Prompt user for an ID.
    - If ID not found, show "ID not found" message.
    - If ID exists, remove it from all 4 lists.
    - Print success message after deletion.

Option 3 - ADD A NEW RECORD: (Write a function that receives all 4 lists.)

    - Ask user for a new ID.
    - If ID already exists, show error message.
    - If ID is new:
        - Append ID to ids.
        - Append default values to other lists:
            Paid = "No", Days = 0, Status = "Active"
    - Show success message after adding.
    
Option 4 - UPDATE STATUS: (Write a function that receives 2 lists: ID and status.)

    - Ask user for an ID.
    - If ID not found, show message.
    - If ID exists, ask for new status and update status list.
    - Show success message.
    
Option 8 - QUIT & SAVE: (Write a function that receives all 4 lists.)

    - Write all 4 lists back to "college.txt" in CSV format.
    - Exit the program after saving.
    
Additional notes:
    - I should not use dictionaries or CSV module.
    - I should only use Python concepts taught in MTU so far.
    - Ensure I do understand all code I have included
"""

# Function to read account details from file.
# Runs once at the start of the program.
# Opens the file, reads each line and splits the data.
# Stores the data into 4 separate lists: players_id, pay_status, days, status.
# Returns the 4 lists to be used in the rest of the program.

def read_accounts(filename):
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

# Option 1
# Function to display all account details.
# Receives the 4 lists and prints each account in a formatted way.
# Shows player type (Pro/Casual), payment status (✅/❎),
# and adds an alert if days since last password reset is over 90.

def view_all_accounts(players_id, pay_status, days, status):

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