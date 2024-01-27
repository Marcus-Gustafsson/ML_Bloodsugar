import sqlite3



class DatabaseManager:

    """
    Manages database connections and transactions.

    Attributes:
        db_name (str): The name of the database file.
    """

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

def setup_database():

    """
    Sets up the database by creating necessary tables.
    """

    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
                user_id INTEGER PRIMARY KEY,
                user_first_name TEXT,
                age TEXT,
                weight TEXT,
                insulin_type TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_inputs (
                entry_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                fat_content TEXT,
                protein_content TEXT,
                carb_content TEXT,
                exercise_intensity TEXT,
                insulin_dose REAL,
                insulin_time TEXT,
                current_blood_sugar REAL,
                blood_sugar_unit TEXT,
                blood_sugar_time TEXT,
                FOREIGN KEY(user_id) REFERENCES user_info(user_id)
            )
        ''')



def user_exists(user_first_name):
    """
    Checks if a user already exists in the database.

    Args:
        user_first_name (str): The first name of the user to check.

    Returns:
        bool: True if the user exists, False otherwise.
    """

    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute("SELECT user_id FROM user_info WHERE user_first_name = ?", (user_first_name,))
        return cursor.fetchone() is not None
    

def get_user_id(user_first_name):

    """
    Retrieves the user ID based on the user's first name.

    Args:
        user_first_name (str): The first name of the user.

    Returns:
        int or None: The user ID if found, otherwise None.
    """

    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute("SELECT user_id FROM user_info WHERE user_first_name = ?", (user_first_name,))
        result = cursor.fetchone()
        return result[0] if result else None



def insert_user_static_info(user_static_info):
    """
    Inserts static user information into the database.

    Args:
        user_static_info (UserStaticInfo): The static information of the user to insert.

    Returns:
        int: The user ID of the inserted user.
    """

    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('''
            INSERT INTO user_info (user_first_name, age, weight, insulin_type)
            VALUES (?, ?, ?, ?)
        ''', (user_static_info.name, user_static_info.age, user_static_info.weight, user_static_info.insulin_type))
        cursor.execute("SELECT last_insert_rowid()")
        return cursor.fetchone()[0]  # This returns the new user_id


def insert_user_daily_input(user_daily_input):
    """
    Inserts daily input data for a user into the database.

    Args:
        user_daily_input (UserDailyInput): The daily input data of the user to insert.
    """

    try:
        with DatabaseManager('blood_sugar_app.db') as cursor:
            cursor.execute('''
                INSERT INTO daily_inputs (user_id, fat_content, protein_content, carb_content, exercise_intensity, insulin_dose, insulin_time, current_blood_sugar, blood_sugar_unit, blood_sugar_time)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_daily_input.user_id, user_daily_input.fat_content, user_daily_input.protein_content, user_daily_input.carb_content, user_daily_input.exercise_intensity, user_daily_input.insulin_dose, user_daily_input.insulin_time, user_daily_input.current_blood_sugar, user_daily_input.blood_sugar_unit, user_daily_input.blood_sugar_time))
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_user_daily_input: {e}")




def get_all_user_inputs():

    """
    Retrieves all user inputs from the database.

    Returns:
        tuple: A tuple containing two elements: a list of column names and a list of data rows.
    """

    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('''
            SELECT u.user_first_name, d.* FROM daily_inputs d
            JOIN user_info u ON d.user_id = u.user_id
        ''')
        columns = [description[0] for description in cursor.description]
        data = cursor.fetchall()
        return columns, data


def print_all_user_data():

    """
    Prints all user data, both static and daily inputs, from the database.
    """

    print("Static User Info:")
    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('SELECT * FROM user_info')
        columns = [description[0] for description in cursor.description]
        for row in cursor.fetchall():
            print(', '.join(f"{col}: {val}" for col, val in zip(columns, row)))

    print("\nDaily Inputs:")
    column_names, user_data = get_all_user_inputs()
    for row in user_data:
        print(', '.join(f"{col}: {val}" for col, val in zip(column_names, row)))