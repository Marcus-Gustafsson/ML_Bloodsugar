import sqlite3


def main():

    # Example of using this function
    #user_input = get_user_input()
    #insert_user_input(user_input)
    print_all_user_data()

    print("END")



class UserInput:
    def __init__(self, name , age, weight, fat_content, protein_content, carb_content, exercise_intensity, insulin_type, insulin_dose, current_blood_sugar, blood_sugar_unit, blood_sugar_time):
        self.name = name
        self.age = age
        self.weight = weight
        self.fat_content = fat_content
        self.protein_content = protein_content
        self.carb_content = carb_content
        self.exercise_intensity = exercise_intensity
        self.insulin_type = insulin_type
        self.insulin_dose = insulin_dose
        self.current_blood_sugar = current_blood_sugar
        self.blood_sugar_unit = blood_sugar_unit
        self.blood_sugar_time = blood_sugar_time  # Time of the blood sugar reading



def get_user_input():
    user_first_name = input("Enter your first name: ")
    age = input("Enter your age: ")
    weight = input("Enter weight (kg): ")
    fat_content = input("Enter fat content of your meal (low, medium, high): ")
    protein_content = input("Enter protein content of your meal (low, medium, high): ")
    carb_content = input("Enter carb content of your meal (low, medium, high): ")
    exercise_intensity = input("Enter your exercise intensity for the next 90 minutes (no exercise, light, medium intensity, high intensity): ")
    insulin_type = input("Enter your insulin type: ")
    insulin_dose = float(input("Enter your insulin dose: "))
    
    # Assuming the blood sugar value and time will be input manually for now
    current_blood_sugar = float(input("Enter your current blood sugar level: "))
    blood_sugar_time = input("Enter the time of your blood sugar reading (e.g., '14:30'): ")
    
    if current_blood_sugar > 30:
        blood_sugar_unit = "mg/dL"
    else:
        blood_sugar_unit = "mmol/L"

    return UserInput(user_first_name, age, weight, fat_content, protein_content, carb_content, exercise_intensity, insulin_type, insulin_dose, current_blood_sugar, blood_sugar_unit, blood_sugar_time)




def insert_user_input(user_input):
    try:
        with DatabaseManager('blood_sugar_app.db') as cursor:
            cursor.execute('''
            INSERT INTO user_input (user_first_name, age, weight, fat_content, protein_content, carb_content, exercise_intensity, insulin_dose, current_blood_sugar, blood_sugar_unit, blood_sugar_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', ( user_input.name, user_input.age, user_input.weight, user_input.fat_content, user_input.protein_content, user_input.carb_content, user_input.exercise_intensity, user_input.insulin_dose, user_input.current_blood_sugar, user_input.blood_sugar_unit, user_input.blood_sugar_time))
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_user_input: {e}")

def get_all_user_inputs():
    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('SELECT * FROM user_input')
        columns = [description[0] for description in cursor.description]
        data = cursor.fetchall()
        #print("DBG: Columns:", columns)  # Debug print
        #print("DBG: Data:", data)  # Debug print
        return columns, data

def print_all_user_data():
    print("DBG: Printing data....")
    column_names, user_data = get_all_user_inputs()
    if not user_data:
        print("DBG: No data found!")
    for row in user_data:
        row_data = [f"{col_name}: {value}" for col_name, value in zip(column_names, row)]
        print(', '.join(row_data))




class DatabaseManager:
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
    with DatabaseManager('blood_sugar_app.db') as cursor:
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS user_input (
                            id INTEGER PRIMARY KEY,
                            user_first_name TEXT,
                            age TEXT,
                            weight TEXT,
                            fat_content TEXT,
                            protein_content TEXT,
                            carb_content TEXT,
                            exercise_intensity TEXT,
                            insulin_dose REAL,
                            current_blood_sugar REAL,
                            blood_sugar_unit TEXT,
                            blood_sugar_time TEXT
                        )
                        ''')

if __name__ == "__main__":
    setup_database()
    main()
