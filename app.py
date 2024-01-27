# app.py

import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QDialog
from PySide6.QtCore import QTimer
from GUI.ui_main_window import Ui_MainWindow  # Replace with your actual import statement
import pyqtgraph as pg
from database import setup_database, insert_user_static_info, insert_user_daily_input, user_exists, get_user_id, print_all_user_data
from user_input import get_user_static_info, get_user_daily_info
from models import UserDailyInput



from GUI.User_input_daily import Ui_Dialog

class DailyValuesDialog(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def get_values(self):
        # Get the values for carbs, protein, and fat content from the UI elements
        carb_content = 'low' if self.ui.pb_carb_low.isChecked() else 'medium' if self.ui.pb_carb_medium.isChecked() else 'high'
        protein_content = 'low' if self.ui.pb_protein_low.isChecked() else 'medium' if self.ui.pb_protein_medium.isChecked() else 'high'
        fat_content = 'low' if self.ui.pb_fat_low.isChecked() else 'medium' if self.ui.pb_fat_medium.isChecked() else 'high'
        exercise_intensity = 'no' if self.ui.pb_exercise_no.isChecked() else 'light' if self.ui.pb_exercise_light.isChecked() else 'medium' if self.ui.pb_exercise_medium.isChecked() else 'high'
        
        # Get the values for insulin dose and blood sugar from the UI elements
        insulin_dose = self.ui.lineedit_insulin_dose.text()
        insulin_time = self.ui.timeEdit_time_of_insulin.time().toString()
        blood_sugar = self.ui.lineEdit_blood_sugar.text()
        blood_sugar_time = self.ui.timeEdit_blood_sugar.time().toString()
        
        return {
            'carb_content': carb_content,
            'protein_content': protein_content,
            'fat_content': fat_content,
            'exercise_intensity': exercise_intensity,
            'insulin_dose': float(insulin_dose) if insulin_dose else 0,
            'insulin_time': insulin_time,
            'blood_sugar': float(blood_sugar) if blood_sugar else 0,
            'blood_sugar_time': blood_sugar_time
        }

    def accept(self):
        values = self.get_values()
        # If insert_user_daily_input accepts a UserDailyInput object, then pass it as such
        daily_input = UserDailyInput(
            user_id=self.user_id,
            fat_content=values['fat_content'],
            protein_content=values['protein_content'],
            carb_content=values['carb_content'],
            exercise_intensity=values['exercise_intensity'],
            insulin_dose=values['insulin_dose'],
            insulin_time=values['insulin_time'],
            current_blood_sugar=values['blood_sugar'],
            blood_sugar_time=values['blood_sugar_time']
        )
        insert_user_daily_input(daily_input)  # Assuming this function takes a UserDailyInput object
        super().accept()
       


class BloodSugarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_database()  # Initialize the database
        self.initUI()

    def initUI(self):
        # Connect signals and slots here
        self.ui.pb_new_user.clicked.connect(self.new_user_clicked)
        self.ui.pb_daily_values.clicked.connect(self.daily_values_clicked)
        self.setup_graph()

    def new_user_clicked(self):
        # This method replaces the first part of your original main() function
        # Open a dialog or another window to get user information, then save it
        pass

    def daily_values_clicked(self):
        user_name = self.ui.lineEdit_current_user.text()  # Retrieve the text from the line edit
        user_id = get_user_id(user_name)  # Retrieve the user ID based on the name
        if user_id is not None:
            dialog = DailyValuesDialog(user_id, self)
            if dialog.exec():
                # Dialog was accepted, proceed to save the data
                values = dialog.get_values()  # get_values is now a method of the dialog instance
                insert_user_daily_input(user_id, **values)
        else:
            print("User not found or invalid user name.")


    def setup_graph(self):
        # Create a PlotWidget object to use for graphing
        self.plot_widget = pg.PlotWidget()
        
        # Create a layout for the QGraphicsView and add the PlotWidget to it
        layout = self.ui.graphicsView_blood_insulin_graph.layout() or QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.ui.graphicsView_blood_insulin_graph.setLayout(layout)
        
        # Here we just plot some random data, replace this with your actual data update logic
        self.x = list(range(100))  # 100 time points
        self.y = np.random.normal(size=100)  # 100 data points
        self.graph = self.plot_widget.plot(self.x, self.y)

        # Set up a timer to update the graph periodically
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Update every second for this example
        self.timer.timeout.connect(self.update_graph)
        self.timer.start()

    def update_graph(self):
        # In a real application, you would update the self.y list with your actual data
        self.y = np.roll(self.y, -1)  # Shift data one place to the left
        self.y[-1] = np.random.normal()  # Add a new random value at the end
        self.graph.setData(self.x, self.y)  # Update the graph

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BloodSugarApp()
    window.show()
    sys.exit(app.exec_())

