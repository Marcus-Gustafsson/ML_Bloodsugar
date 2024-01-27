
from models import UserStaticInfo, UserDailyInput


def get_user_static_info(user_first_name):


    """
    Gets static information about the user from input.

    Args:
        user_first_name (str): The first name of the user.

    Returns:
        UserStaticInfo: An instance of UserStaticInfo containing the user's static data.
    """

    age = input("Enter your age: ")
    weight = input("Enter weight (kg): ")
    insulin_type = input("Enter your insulin type: ")

    return UserStaticInfo(user_first_name, age, weight, insulin_type)


def get_user_daily_info(user_id):

    """
    Gets daily user data from input.

    Args:
        user_id (int): The ID of the user for whom to collect daily data.

    Returns:
        UserDailyInput: An instance of UserDailyInput containing the user's daily data.
    """

    fat_content = input("Enter fat content of your meal (low, medium, high): ")
    protein_content = input("Enter protein content of your meal (low, medium, high): ")
    carb_content = input("Enter carb content of your meal (low, medium, high): ")
    exercise_intensity = input("Enter your exercise intensity for the next 90 minutes (no exercise, light, medium intensity, high intensity): ")
    insulin_dose = float(input("Enter your insulin dose: "))
    insulin_time = input("Enter time of your insulin dose (e.g., '11:00'): ")
    # Assuming the blood sugar value and time will be input manually for now
    current_blood_sugar = float(input("Enter your current blood sugar level: "))
    blood_sugar_time = input("Enter the time of your blood sugar reading (e.g., '14:30'): ")
    
    if current_blood_sugar > 30:
        blood_sugar_unit = "mg/dL"
    else:
        blood_sugar_unit = "mmol/L"

    return UserDailyInput(user_id, fat_content, protein_content, carb_content, exercise_intensity, insulin_dose, insulin_time, current_blood_sugar, blood_sugar_unit, blood_sugar_time)