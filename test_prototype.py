"""Automated tests for the CareQueue proof of concept."""
import sqlite3
import unittest
from prototype import create_database, register_patient, book_appointment, check_in


class TestCareQueue(unittest.TestCase):
    def setUp(self):
        self.db = create_database()
        self.patient_id = register_patient(self.db, "Test Patient")

    def tearDown(self):
        self.db.close()

    def test_patient_registration(self):
        name = self.db.execute("SELECT name FROM patients WHERE id = ?", (self.patient_id,)).fetchone()[0]
        self.assertEqual(name, "Test Patient")

    def test_booking_and_duplicate_prevention(self):
        book_appointment(self.db, self.patient_id, "Dr. Lee", "2026-10-20 09:00")
        with self.assertRaises(sqlite3.IntegrityError):
            book_appointment(self.db, self.patient_id, "Dr. Lee", "2026-10-20 09:00")

    def test_check_in_once(self):
        appt_id = book_appointment(self.db, self.patient_id, "Dr. Lee", "2026-10-20 09:00")
        self.assertTrue(check_in(self.db, appt_id))
        self.assertFalse(check_in(self.db, appt_id))
        status = self.db.execute("SELECT status FROM appointments WHERE id = ?", (appt_id,)).fetchone()[0]
        self.assertEqual(status, "checked_in")


if __name__ == "__main__":
    unittest.main()
