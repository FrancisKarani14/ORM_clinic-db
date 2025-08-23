import sqlite3

CONN = sqlite3.connect("clinic.db")
CURSOR = CONN.cursor()