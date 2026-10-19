"""CareQueue classroom proof of concept (Python 3 + SQLite)."""
import sqlite3


def create_database():
    db = sqlite3.connect(":memory:")
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("CREATE TABLE patients (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    db.execute("""CREATE TABLE appointments (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        provider TEXT NOT NULL,
        start_time TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'scheduled',
        UNIQUE(provider, start_time),
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )""")
    return db


def register_patient(db, name):
    return db.execute("INSERT INTO patients (name) VALUES (?)", (name,)).lastrowid


def book_appointment(db, patient_id, provider, start_time):
    return db.execute(
        "INSERT INTO appointments (patient_id, provider, start_time) VALUES (?, ?, ?)",
        (patient_id, provider, start_time),
    ).lastrowid


def check_in(db, appointment_id):
    return db.execute(
        "UPDATE appointments SET status = 'checked_in' "
        "WHERE id = ? AND status = 'scheduled'", (appointment_id,)
    ).rowcount == 1


def main():
    with create_database() as db:
        patient_id = register_patient(db, "Sample Patient")
        appt_id = book_appointment(db, patient_id, "Dr. Lee", "2026-10-20 09:00")
        print("Appointment booked.")
        try:
            book_appointment(db, patient_id, "Dr. Lee", "2026-10-20 09:00")
        except sqlite3.IntegrityError:
            print("Duplicate provider/time booking blocked.")
        print("Appointments:", db.execute("SELECT * FROM appointments").fetchall())
        print("Checked in successfully." if check_in(db, appt_id) else "Check-in rejected.")
        print("Repeat check-in rejected." if not check_in(db, appt_id) else "Checked in again.")
    db.close()


if __name__ == "__main__":
    main()
