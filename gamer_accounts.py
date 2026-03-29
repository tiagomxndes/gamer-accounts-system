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