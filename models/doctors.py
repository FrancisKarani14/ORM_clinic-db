from db import CURSOR, CONN

# create the doctro class

class Doctor:
    def __init__(self, first_name, second_name, specialization, id=None):
        self.id = id
        self.First_name = first_name
        self.second_name = second_name
        self.specialization = specialization
        
    def __repr__(self):
        return f"<Doctor {self.First_name}, {self.second_name}, {self.specialization}>"
    
    # class method to create a table
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS doctors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        specialization_name TEXT NOT NULL,

        );
        """
        CURSOR.execute(sql)
        CONN.commit()

        # create the columns

        def save(self):
            sql ="""
            INSERT OR IGNORE into Doctors(first_name, second_name, speialization)
            VALUES(?,?,?);
            """
            CURSOR.execute(sql)
            CONN.commit()

            if CURSOR.lastrowid:
                self.id = CURSOR.lastrowid
            elif self.id is None:
                row = CURSOR.execute(
                  "SELECT id FROM doctors WHERE first_name = ? AND second_name = ?",
                   (self.first_name, self.second_name)
                ).fetchone()
