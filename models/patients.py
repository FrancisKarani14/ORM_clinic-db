from db import CURSOR, CONN
# after importing CURSOR AND CONN
# create a class called patient which will later be the table


class Patient:
    def __init__(self, first_name, second_name, disease, id=None):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.disease = disease
# method that will help to show how the class will look lik if it is printed
    def __repr__(self):
        return f"<Doctor {self.first_name}, {self.second_name}, {self.disease}>"
# a class method to create a table for patients 
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTING patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        disease TEXT NOT NULL;

        );
        """
        CURSOR.execute(sql)
        CONN.commit()

# An instance method to insert the class instances
    def save(self):
        sql = """
        INSERT OR IGNORE INTO patients (first_name, second_name, disease)
        VALUES(?,?,?)
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
            if row:
                self.id = row[0]
    
           
