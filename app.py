# app.py

import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QDialog
from PySide6.QtCore import QTimer
from GUI.Main_window_ui import Ui_MainWindow  # Replace with your actual import statement
import pyqtgraph as pg
from database import setup_database, insert_user_static_info, insert_user_daily_input, user_exists, get_user_id, print_all_user_data, get_all_user_names, get_latest_input_for_user
from models import UserDailyInput, UserStaticInfo
from GUI.User_input_daily_ui import Ui_daily_dialog
from GUI.User_input_static_ui import Ui_static_dialog

class UserStaticDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_static_dialog()
        self.ui.setupUi(self)
        # Additional setup can be done here

    def get_values(self):
        name = self.ui.lineEdit_user_name.text()
        date_of_birth = self.ui.dateEdit_date_of_birth.date().toString("yyyy-MM-dd")
        weight = self.ui.lineEdit_weight.text()
        insulin_type = self.ui.comboBox_insulin_type.currentText()
        insulin_to_carb_ratio = self.ui.lineEdit_insulin_to_carb_ratio.text()
        blood_sugar_unit = "mmol/L" if self.ui.checkBox_mmol_unit.isChecked() else "mg/dL"
        
        return {
            'name': name,
            'date_of_birth': date_of_birth,
            'weight': weight,
            'insulin_type': insulin_type,
            'insulin_to_carb_ratio': insulin_to_carb_ratio,
            'blood_sugar_unit': blood_sugar_unit
        }

    def accept(self):
        values = self.get_values()
        print("User Static Info:", values)  # Debug print
        static_info = UserStaticInfo(**values)
        success = insert_user_static_info(static_info)
        if success:
            super().accept()
        else:
            print("Error saving user _static_ information.")




class DailyValuesDialog(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.ui = Ui_daily_dialog()
        self.ui.setupUi(self)


        # Additional setup can be done here
        self.selected_buttons = {
            'carb': None,
            'fat': None,
            'protein': None,
            'exercise': None
        }

        self.ui.pb_carb_low.setCheckable(True)
        self.ui.pb_carb_medium.setCheckable(True)
        self.ui.pb_carb_high.setCheckable(True)

        self.ui.pb_protein_low.setCheckable(True)
        self.ui.pb_protein_medium.setCheckable(True)
        self.ui.pb_protein_high.setCheckable(True)

        self.ui.pb_fat_low.setCheckable(True)
        self.ui.pb_fat_medium.setCheckable(True)
        self.ui.pb_fat_high.setCheckable(True)

        self.ui.pb_exercise_no.setCheckable(True)
        self.ui.pb_exercise_light.setCheckable(True)
        self.ui.pb_exercise_medium.setCheckable(True)
        self.ui.pb_exercise_high.setCheckable(True)


        # Connect carb content button signals
        self.ui.pb_carb_low.clicked.connect(lambda: self.handle_button_click('carb', self.ui.pb_carb_low))
        self.ui.pb_carb_medium.clicked.connect(lambda: self.handle_button_click('carb', self.ui.pb_carb_medium))
        self.ui.pb_carb_high.clicked.connect(lambda: self.handle_button_click('carb', self.ui.pb_carb_high))

        # Connect protein content button signals
        self.ui.pb_protein_low.clicked.connect(lambda: self.handle_button_click('protein', self.ui.pb_protein_low))
        self.ui.pb_protein_medium.clicked.connect(lambda: self.handle_button_click('protein', self.ui.pb_protein_medium))
        self.ui.pb_protein_high.clicked.connect(lambda: self.handle_button_click('protein', self.ui.pb_protein_high))

        # Connect fat content button signals
        self.ui.pb_fat_low.clicked.connect(lambda: self.handle_button_click('fat', self.ui.pb_fat_low))
        self.ui.pb_fat_medium.clicked.connect(lambda: self.handle_button_click('fat', self.ui.pb_fat_medium))
        self.ui.pb_fat_high.clicked.connect(lambda: self.handle_button_click('fat', self.ui.pb_fat_high))

        # Connect exercise intensity button signals
        self.ui.pb_exercise_no.clicked.connect(lambda: self.handle_button_click('exercise', self.ui.pb_exercise_no))
        self.ui.pb_exercise_light.clicked.connect(lambda: self.handle_button_click('exercise', self.ui.pb_exercise_light))
        self.ui.pb_exercise_medium.clicked.connect(lambda: self.handle_button_click('exercise', self.ui.pb_exercise_medium))
        self.ui.pb_exercise_high.clicked.connect(lambda: self.handle_button_click('exercise', self.ui.pb_exercise_high))


    

    def handle_button_click(self, category, clicked_button):
        # Debug print to verify which button is clicked
        print(f"DBG: {category} button clicked: {clicked_button.objectName()}")

        # Reset all buttons in the category
        self.reset_button_states_in_category(category)
        
        # Update the selected button reference
        self.selected_buttons[category] = clicked_button
        
        # Disable the clicked button and change its style
        clicked_button.setEnabled(False)
        clicked_button.setStyleSheet("background-color: #004C99; color: #7F7F7F;")

    def reset_button_states_in_category(self, category):
        button_group = self.get_button_group(category)
        for button in button_group:
            button.setEnabled(True)
            button.setChecked(False)
            button.setStyleSheet("")  # Reset style to default

    def get_button_group(self, category):
        if category == 'carb':
            return [self.ui.pb_carb_low, self.ui.pb_carb_medium, self.ui.pb_carb_high]
        elif category == 'protein':
            return [self.ui.pb_protein_low, self.ui.pb_protein_medium, self.ui.pb_protein_high]
        elif category == 'fat':
            return [self.ui.pb_fat_low, self.ui.pb_fat_medium, self.ui.pb_fat_high]
        elif category == 'exercise':
            return [self.ui.pb_exercise_no, self.ui.pb_exercise_light, self.ui.pb_exercise_medium, self.ui.pb_exercise_high]


    def get_values(self):
        # Debug print to verify the state of selected buttons
        print(f"DBG: Selected buttons before getting values: {self.selected_buttons}")

        # Use the selected_buttons dictionary to get the content values
        carb_content = 'Low' if self.selected_buttons['carb'] == self.ui.pb_carb_low else 'Medium' if self.selected_buttons['carb'] == self.ui.pb_carb_medium else 'High'
        protein_content = 'Low' if self.selected_buttons['protein'] == self.ui.pb_protein_low else 'Medium' if self.selected_buttons['protein'] == self.ui.pb_protein_medium else 'High'
        fat_content = 'Low' if self.selected_buttons['fat'] == self.ui.pb_fat_low else 'Medium' if self.selected_buttons['fat'] == self.ui.pb_fat_medium else 'High'
        exercise_intensity = 'No' if self.selected_buttons['exercise'] == self.ui.pb_exercise_no else 'Light' if self.selected_buttons['exercise'] == self.ui.pb_exercise_light else 'Medium' if self.selected_buttons['exercise'] == self.ui.pb_exercise_medium else 'High'
        
        # Get the values for insulin dose and blood sugar from the UI elements
        insulin_dose = self.ui.lineedit_insulin_dose.text()
        insulin_time = self.ui.timeEdit_time_of_insulin.time().toString()
        blood_sugar = self.ui.lineEdit_blood_sugar.text()
        blood_sugar_time = self.ui.timeEdit_blood_sugar.time().toString()
        
        values = {
            'user_id': self.user_id,
            'carb_content': carb_content,
            'protein_content': protein_content,
            'fat_content': fat_content,
            'exercise_intensity': exercise_intensity,
            'insulin_dose': float(insulin_dose) if insulin_dose else 0,
            'insulin_time': insulin_time,
            'blood_sugar': float(blood_sugar) if blood_sugar else 0,
            'blood_sugar_time': blood_sugar_time
        }

        # Debug print to verify the values being returned
        print(f"DBG: Values obtained from dialog: {values}")
        return values

    def accept(self):
        values = self.get_values()
        print("User Static Info:", values)  # Debug print
        daily_input = UserDailyInput(**values)
        success = insert_user_daily_input(daily_input)
        if success:
            super().accept()
        else:
            print("Error saving user _daily_ information.")
       


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
        self.populate_user_combobox()
        # Connect the user selection change signal
        self.ui.comboBox_current_user.currentIndexChanged.connect(self.on_user_selection_changed)
        self.update_latest_input()

    def populate_user_combobox(self):
        user_names = get_all_user_names()
        self.ui.comboBox_current_user.clear()
        self.ui.comboBox_current_user.addItems(user_names)

    def update_latest_input(self):
        user_name = self.ui.comboBox_current_user.currentText()
        user_id = get_user_id(user_name)
        latest_input = get_latest_input_for_user(user_id)
        print(f"DBG: Latest input: {latest_input}")
        
        # Format the output
        if latest_input:
            formatted_output = (
                f"Last meal (Carb/Protein/Fat): {latest_input.get('carb_content', '')}/{latest_input.get('protein_content', '')}/{latest_input.get('fat_content', '')}, "
                f"Exercise next 90min: {latest_input.get('exercise_intensity', '')}, "
                f"insulin dose: {latest_input.get('insulin_dose', '')} units, "
                f"dose time: {latest_input.get('insulin_time', '')}, "
                f"Blood sugar reading: {latest_input.get('blood_sugar', '')}, "
                f"reading time: {latest_input.get('blood_sugar_time', '')}"
            )
        else:
            formatted_output = "No data available"

        self.ui.lineEdit_latest_input.setText(formatted_output)


    def on_user_selection_changed(self, index):
        self.update_latest_input()

    def new_user_clicked(self):
        static_dialog = UserStaticDialog(self)
        if static_dialog.exec():
            self.populate_user_combobox()
            self.update_latest_input()

    def daily_values_clicked(self):
        user_name = self.ui.comboBox_current_user.currentText()
        user_id = get_user_id(user_name)
        if user_id is not None:
            daily_dialog = DailyValuesDialog(user_id, self)
            if daily_dialog.exec():
                self.update_latest_input()
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
    sys.exit(app.exec())

