import sqlite3
# creates a connection to the database and allows sql commands to be used

CONN = sqlite3.connect("clinic.db")
CURSOR = CONN.cursor()