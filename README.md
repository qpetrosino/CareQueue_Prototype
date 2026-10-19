CareQueue — Clinic Appointment Scheduling & Patient Check-In
CISC 371 | Phase 1: Coding Environment Proof
Project Overview
CareQueue is a classroom prototype for a small outpatient clinic. This initial Python program demonstrates registering a fictional patient, booking a provider appointment, preventing conflicting bookings, and checking a patient in.

This is a command-line proof of concept, not a completed web application.
Requirements
- Python 3
- SQLite (included through Python's built-in sqlite3 module)
- No third-party packages or installation steps required
Files
- prototype.py — Creates an in-memory SQLite database and demonstrates the appointment workflow.
- test_prototype.py — Three automated unit tests using Python's built-in unittest framework.
How to Run
1. Save prototype.py and test_prototype.py in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run the prototype:
   python prototype.py
4. Run the automated tests:
   python -m unittest -v test_prototype.py
On systems where the python command is unavailable, use python3 instead.
Features Demonstrated
- Patient registration: Adds a fictional patient to the database.
- Appointment booking: Assigns a patient, provider, and appointment time.
- Duplicate booking protection: Rejects a second booking for the same provider and time slot.
- Appointment viewing: Displays stored appointment records in the terminal.
- Patient check-in: Changes a scheduled appointment to checked_in.
- Repeat check-in protection: Rejects checking in the same appointment twice.
Automated Tests
The test file contains three tests:
1. test_patient_registration — Checks that a patient is saved correctly.
2. test_booking_and_duplicate_prevention — Checks that conflicting bookings are rejected.
3. test_check_in_once — Checks successful check-in and rejection of repeated check-in.
A successful test run ends with Ran 3 tests and OK.
Current Limitations
- Uses an in-memory SQLite database; data is erased when the program ends.
- Does not yet include a graphical or browser-based interface.
- Does not yet implement appointment cancellation, appointment searches by date, or staff login.
- Provider names are stored directly in appointments rather than in a separate provider table.
Planned Development
Future work includes a front-desk interface, a persistent database, fuller appointment management, field validation, and additional automated tests.
Privacy Note
All patient details used in this prototype are fictional. Do not enter real patient information. This is a class project, not a production clinical system.
