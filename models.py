class UserStaticInfo:

    """
    Represents static information about a user.

    Attributes:
        name (str): The user's name.
        age (str): The user's age.
        weight (str): The user's weight in kilograms.
        insulin_type (str): The type of insulin used by the user.
        blood_sugar_unit (str): The unit of the blood sugar measurement.
    """

    def __init__(self, name, age, weight, insulin_type, blood_sugar_unit):
        self.name = name
        self.age = age
        self.weight = weight
        self.insulin_type = insulin_type
        self.blood_sugar_unit = blood_sugar_unit

class UserDailyInput:

    """
    Represents daily input data for a user.

    Attributes:
        user_id (int): The ID of the user to whom this daily input belongs.
        fat_content (str): Fat content of the user's meal.
        protein_content (str): Protein content of the user's meal.
        carb_content (str): Carb content of the user's meal.
        exercise_intensity (str): The intensity of exercise.
        insulin_dose (float): The dose of insulin taken.
        insulin_time (str): The time of the insulin dose.
        current_blood_sugar (float): The current blood sugar level.
        blood_sugar_time (str): The time of the blood sugar reading.
    """

    def __init__(self, user_id, fat_content, protein_content, carb_content, exercise_intensity, insulin_dose, insulin_time, current_blood_sugar, blood_sugar_time):
        self.user_id = user_id
        self.fat_content = fat_content
        self.protein_content = protein_content
        self.carb_content = carb_content
        self.exercise_intensity = exercise_intensity
        self.insulin_dose = insulin_dose
        self.insulin_time = insulin_time
        self.current_blood_sugar = current_blood_sugar
        self.blood_sugar_time = blood_sugar_time
