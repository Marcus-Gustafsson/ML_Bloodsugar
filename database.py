import sqlite3



class DataBaseManager:

    """
    Mandate_of_births database connections and transactions.

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

    with DataBaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
                user_id INTEGER PRIMARY KEY,
                user_first_name TEXT,
                date_of_birth TEXT,
                weight TEXT,
                insulin_type TEXT,
                insulin_to_carb_ratio TEXT,
                blood_sugar_unit TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_inputs (
                entry_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                time_of_meal TEXT,
                fat_content TEXT,
                protein_content TEXT,
                carb_content TEXT,
                exercise_intensity TEXT,
                insulin_dose REAL,
                insulin_time TEXT,
                blood_sugar REAL,
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

    with DataBaseManager('blood_sugar_app.db') as cursor:
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

    with DataBaseManager('blood_sugar_app.db') as cursor:
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
    try:
        with DataBaseManager('blood_sugar_app.db') as cursor:
            cursor.execute('''
                INSERT INTO user_info (user_first_name, date_of_birth, weight, insulin_type, insulin_to_carb_ratio, blood_sugar_unit)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_static_info.name, user_static_info.date_of_birth, user_static_info.weight, user_static_info.insulin_type, user_static_info.insulin_to_carb_ratio, user_static_info.blood_sugar_unit))
            cursor.execute("SELECT last_insert_rowid()")
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def insert_user_daily_input(user_daily_input):
    """
    Inserts daily input data for a user into the database.

    Args:
        user_daily_input (UserDailyInput): The daily input data of the user to insert.
    """

    try:
        with DataBaseManager('blood_sugar_app.db') as cursor:
            cursor.execute('''
                INSERT INTO daily_inputs (user_id, time_of_meal, carb_content, protein_content, fat_content, exercise_intensity, insulin_dose, insulin_time, blood_sugar, blood_sugar_time)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_daily_input.user_id, user_daily_input.time_of_meal, user_daily_input.carb_content, user_daily_input.protein_content, user_daily_input.fat_content, user_daily_input.exercise_intensity, user_daily_input.insulin_dose, user_daily_input.insulin_time, user_daily_input.blood_sugar, user_daily_input.blood_sugar_time))
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Exception in insert_user_daily_input: {e}")
        return False
    

def get_all_user_names():
    """
    Retrieves all user names from the database.

    Returns:
        list: A list of user names.
    """
    try:
        with DataBaseManager('blood_sugar_app.db') as cursor:
            cursor.execute("SELECT user_first_name FROM user_info")
            return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    

def get_latest_input_for_user(user_id):
    """
    Retrieves the latest input data for a given user.

    Args:
        user_id (int): The user ID.

    Returns:
        dict: A dictionary containing the latest input data for the user.
    """
    try:
        with DataBaseManager('blood_sugar_app.db') as cursor:
            cursor.execute('''
                SELECT * FROM daily_inputs 
                WHERE user_id = ? 
                ORDER BY blood_sugar_time DESC 
                LIMIT 1
            ''', (user_id,))
            row = cursor.fetchone()
            if row:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, row))
            return {}
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {}




def get_all_user_inputs():

    """
    Retrieves all user inputs from the database.

    Returns:
        tuple: A tuple containing two elements: a list of column names and a list of data rows.
    """

    with DataBaseManager('blood_sugar_app.db') as cursor:
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
    with DataBaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('SELECT * FROM user_info')
        columns = [description[0] for description in cursor.description]
        for row in cursor.fetchall():
            print(', '.join(f"{col}: {val}" for col, val in zip(columns, row)))

    print("\nDaily Inputs:")
    column_names, user_data = get_all_user_inputs()
    for row in user_data:
        print(', '.join(f"{col}: {val}" for col, val in zip(column_names, row)))