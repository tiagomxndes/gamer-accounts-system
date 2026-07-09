# Gamer Accounts System

A command-line tool for managing player accounts on an online gaming platform. Built in Python using only core language features — no external libraries, no dictionaries, just lists and functions.

This was my first-year project for the Software Development degree at MTU (Munster Technological University).

## Overview

The system reads account data from a CSV-style text file (college.txt) and loads it into memory, where it can be viewed, updated, and exported through an interactive menu. All changes are saved back to the file on exit.

Data format: ID, Paid, Days, Status

| Field | Description |
|---|---|
| ID | Player identifier — starts with PRO (professional) or CAS (casual) |
| Paid | Membership status — Yes or No |
| Days | Days since last password reset |
| Status | Account status — Active, Locked, or Disabled |

## Features

1. View All Accounts
Displays every account in a formatted table — payment status shown with symbols, player type identified (Pro/Casual), and an alert for any account over 90 days since its last password reset.

2. Delete a Record
Remove an account by ID. Displays an error if the ID doesn't exist.

3. Add a New Record
Create a new account with a unique ID. New accounts default to Paid = No, Days = 0, Status = Active.

4. Update Status
Change an existing account's status by ID.

5. Player Type Percentages
Calculates and displays what percentage of accounts are Professional vs Casual.

6. Export Accounts by Status
Writes player IDs into separate files based on status: active.txt, locked.txt, disabled.txt.

7. Disable Unpaid Accounts
Automatically disables any account that is Active but hasn't paid, and reports how many accounts were updated.

8. Save and Quit
Writes all current data back to college.txt in CSV format and exits.

## Design Notes

This project was built under a specific set of constraints:
- No dictionaries — data is stored and managed using four parallel lists (players_id, pay_status, days, status)
- No CSV module — file parsing is done manually with string splitting
- Only core Python concepts (functions, loops, conditionals, file I/O)

These constraints were part of the assignment brief, not a design preference — a dictionary- or class-based approach would simplify a lot of this logic, and is something I plan to revisit as a refactor exercise once I've covered OOP.

## Running the Project

python gamer_accounts.py

Make sure college.txt exists in the same directory, formatted as one account per line:
PRO001,Yes,15,Active
CAS002,No,120,Active
