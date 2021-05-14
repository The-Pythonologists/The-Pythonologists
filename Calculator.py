import sys

import math
import numexpr as ne
from datetime import datetime, date

from PySide6.QtGui import (QAction, QFont, QIcon, QPalette, QColor)
from PySide6.QtCore import (Qt, Slot, QRect)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton,
                               QSizePolicy, QMenuBar, QColorDialog, QComboBox, QLabel, QScrollArea)


class Calculator(QMainWindow):
    # ** CLASS PROPERTIES **
    def _QMainWindow_properties(self):
        # -- Assigning our QWidget's properties --
        QWidget.setWindowTitle(self, "Αριθμομηχανή")
        QWidget.setWindowIcon(self, QIcon('assets/CalcIcon.png'))
        QWidget.setGeometry(self, 450, 220, 330, 330)
        # --------------------------------------

    # ** DECLARATION FUNCTIONS **
    def _calculator_modes_declarations(self):
        # ** DECLARATION & ALTERING OF THE CALCULATOR ATTRIBUTES **
        # It contains all the common attributes across calculator modes

        # -- Boolean attributes --
        self.bool_waiting_for_operand = False  # Set to False so it doesn't display a symbol that's pressed on its first run
        self.bool_equal_last_pressed = False  # To check whether the last symbol pressed was a '=' sign
        self.bool_plus_last_pressed = False  # To check whether the last symbol pressed was a '+' sign
        self.bool_minus_last_pressed = False  # To check whether the last symbol pressed was a '-' sign
        self.bool_times_last_pressed = False  # To check whether the last symbol pressed was a '*' sign
        self.bool_division_last_pressed = False  # To check whether the last symbol pressed was a '/' sign
        self.bool_modular_last_pressed = False  # To check whether the last symbol pressed was a 'Mod' sign
        # ------------------------

        # -- String attributes --
        #   For the standard and scientific calculator modes
        self.string_display_box = ''  # Contains the contents of the 'display_box'
        self.string_symbol_box = ''  # Contains the contents of the 'symbol_box'
        self.string_result = ''  # Contains the contents of the complete string
        self.string_last_operand_used = ''  # Contains the contents of the last operand used (excluding = operand)
        self.string_last_number_used = ''  # Contains the contents of the last number used
        self.string_calculated_invoked = ''  # Contains the contents of the function '_calculated_invoked'

        #   For the temperature calculator mode
        self.string_display_box_TEMP = ''  # Contains the contents of the 'display_box_TEMP'
        self.string_symbol_box_TEMP = ''  # Contains the contents of the 'symbol_box_TEMP'

        #   For the time calculator mode
        self.string_display_box_TIME = ''  # Contains the contents of the 'display_box_TIME'
        self.string_symbol_box_TIME = ''  # Contains the contents of the 'symbol_box_TIME'

        #   For the volume calculator mode
        self.string_display_box_VOL = ''  # Contains the contents of the 'display_box_VOL''
        self.string_symbol_box_VOL = ''  # Contains the contents of the 'symbol_box_VOL'

        #   For the data calculator mode
        self.string_display_box_DATA = ''  # Contains the contents of the 'display_box_DATA'
        self.string_symbol_box_DATA = ''  # Contains the contents of the 'symbol_box_DATA'

        #   For the discount calculator mode
        self.string_display_box_DISC = ''  # Contains the contents of the 'display_box_DISC'
        self.string_display_box_DISC_2 = ''  # Contains the contents of the 'display_box_DISC_2'

        #   For the age calculator mode
        self.string_display_box_AGE = ''  # Contains the contents of the 'display_box_AGE'
        self.string_display_box_AGE_2 = ''  # Contains the contents of the 'display_box_AGE_2'

        #   For the mass calculator mode
        self.string_display_box_MASS = ''  # Contains the contents of the 'display_box_MASS'
        self.string_symbol_box_MASS = ''  # Contains the contents of the 'symbol_box_MASS'

        # For the speed calculator mode
        self.string_display_box_SPEED = ''  # Contains the contents of the 'display_box_SPEED'
        self.string_symbol_box_SPEED = ''  # Contains the contents of the 'symbol_box_SPEED'

        #   For the length calculator mode
        self.string_display_box_LEN = ''  # Contains the contents of the 'display_box_LEN'
        self.string_symbol_box_LEN = ''  # Contains the contents of the 'symbol_box_LEN'

        #   For the BMI calculator mode
        self.string_display_box_BMI = ''  # Contains the contents of the 'display_box_BMI'
        self.string_display_box_BMI_2 = ''  # Contains the contents of the 'display_box_BMI_2'
        # -----------------------

        # -- Integer attributes --
        # Declaration of count for the correct use of brackets in scientific mode
        self.left_bracket_count = 0
        self.right_bracket_count = 0

        # Declaration of count for the CE button
        self.clear_entry_count = 0
        # ------------------------

        # -- QFont attribute --
        self.font_button = QFont()
        # ---------------------

        # -- QLineEdit attributes --
        #   For the standard and scientific calculator modes
        self.display_box = QLineEdit('')
        self.symbol_box = QLineEdit('')

        #   For the temperature calculator mode
        self.display_box_temperature = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_temperature = QLineEdit('')

        #   For the time calculator mode
        self.display_box_time = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_time = QLineEdit('')

        #   For the volume calculator mode
        self.display_box_volume = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_volume = QLineEdit('')

        #   For the data calculator mode
        self.display_box_data = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_data = QLineEdit('')

        #   For the discount calculator mode
        self.display_box_discount = QLineEdit('Εισάγετε την αρχική τιμή εδώ.')
        self.display_box_discount1 = QLineEdit('Εισάγετε την έκπτωση εδώ.')
        self.symbol_box_discount = QLineEdit('')

        #   For the age calculator mode
        self.symbol_box_age = QLineEdit('Εισάγετε ημερομηνία γέννησης (Η/Μ/Ε) εδώ')

        #   For the mass calculator mode
        self.display_box_mass = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_mass = QLineEdit('')

        #   For the speed calculator mode
        self.display_box_speed = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_speed = QLineEdit('')

        #   For the length calculator mode
        self.display_box_length = QLineEdit('Εισάγετε την τιμή σας εδώ.')
        self.symbol_box_length = QLineEdit('')

        #   For the BMI calculator mode
        self.display_box_bmi = QLineEdit('Εισάγετε το βάρος εδώ.')
        self.display_box_bmi1 = QLineEdit('Εισάγετε το ύψος εδώ.')
        self.symbol_box_bmi = QLineEdit('')
        # --------------------------

        # -- QMenuBar attribute --
        self.menu_bar = QMenuBar()
        # ------------------------

        # -- QPushButton attributes --
        #       * Number buttons
        """ The number buttons are already assigned in the '_QPushButton_button_nums' """

        #       * Algebraic buttons
        self.button_exponent = QPushButton('x²')
        self.button_raise = QPushButton('xⁿ')
        self.button_absolute = QPushButton('|x|')
        self.button_sqrt = QPushButton('√')
        self.button_log = QPushButton('log')
        self.button_ln = QPushButton('ln')
        self.button_pi = QPushButton('π')
        self.button_factorial = QPushButton('e')

        #       * Trigonometric buttons
        self.button_sin = QPushButton('sin')
        self.button_cos = QPushButton('cos')
        self.button_tan = QPushButton('tan')

        #       * Operand buttons
        self.button_equal = QPushButton('=')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_times = QPushButton('*')
        self.button_division = QPushButton('/')
        self.button_modular = QPushButton('Mod')
        self.button_percent = QPushButton('%')

        #       * Symbol buttons
        self.button_clear_entry = QPushButton('CE')
        self.button_clear = QPushButton('C')
        self.button_backspace = QPushButton('⌫')
        self.button_inverse = QPushButton('+/-')
        self.button_dot = QPushButton('.')
        self.button_left_bracket = QPushButton('(')
        self.button_right_bracket = QPushButton(')')

        #       * Temperature buttons
        self.button_temperature_calculate = QPushButton('Υπολογισμός Θερμοκρασίας')

        #       * Time buttons
        self.button_time_calculate = QPushButton('Υπολογισμός Χρόνου')

        #       * Volume buttons
        self.button_volume_calculate = QPushButton('Υπολογισμός Όγκου')

        #       * Data buttons
        self.button_data_calculate = QPushButton('Υπολογισμός Δεδομένων')

        #       * Discount buttons
        self.button_discount_calculate = QPushButton('Υπολογισμός Έκπτωσης')

        #       * Age buttons
        self.button_age_calculate = QPushButton('Υπολογισμός Ηλικίας')
        self.button_age_clear = QPushButton('Καθαρισμός οθόνης')

        #       * Mass buttons
        self.button_mass_calculate = QPushButton('Υπολογισμός Μάζας')

        #       * Speed buttons
        self.button_speed_calculate = QPushButton('Υπολογισμός Ταχύτητας')

        #       * Length buttons
        self.button_length_calculate = QPushButton('Υπολογισμός Μήκους')

        #       * BMI buttons
        self.button_bmi_calculate = QPushButton('Υπολογισμός ΔΜΣ')
        # ----------------------------

        # -- QComboBox attributes --
        #       * Temperature buttons
        self.button_temperature_first = QComboBox()
        self.button_temperature_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_temperature_first.addItem('Κέλβιν')
        self.button_temperature_first.addItem('Κελσίου')
        self.button_temperature_first.addItem('Φαρενάιτ')
        self.button_temperature_first.setCurrentIndex(0)

        self.button_temperature_second = QComboBox()
        self.button_temperature_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_temperature_second.addItem('Κέλβιν')
        self.button_temperature_second.addItem('Κελσίου')
        self.button_temperature_second.addItem('Φαρενάιτ')
        self.button_temperature_second.setCurrentIndex(0)

        #       * Time buttons
        self.button_time_first = QComboBox()
        self.button_time_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_time_first.addItem('Δευτερόλεπτα')
        self.button_time_first.addItem('Λεπτά')
        self.button_time_first.addItem('Ώρες')
        self.button_time_first.addItem('Μέρες')
        self.button_time_first.addItem('Μήνες')
        self.button_time_first.addItem('Χρόνια')
        self.button_time_first.setCurrentIndex(0)

        self.button_time_second = QComboBox()
        self.button_time_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_time_second.addItem('Δευτερόλεπτα')
        self.button_time_second.addItem('Λεπτά')
        self.button_time_second.addItem('Ώρες')
        self.button_time_second.addItem('Μέρες')
        self.button_time_second.addItem('Μήνες')
        self.button_time_second.addItem('Χρόνια')
        self.button_time_second.setCurrentIndex(0)

        #       * Volume buttons
        self.button_volume_first = QComboBox()
        self.button_volume_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_volume_first.addItem("Κυβικό Μέτρο")
        self.button_volume_first.addItem("Κυβικό Εκατοστό")
        self.button_volume_first.addItem("Λίτρο")
        self.button_volume_first.addItem("Κυβικό Πόδι")
        self.button_volume_first.addItem("Κυβική Ίντσα")
        self.button_volume_first.addItem("Κυβική Γιάρδα")
        self.button_volume_first.setCurrentIndex(0)

        self.button_volume_second = QComboBox()
        self.button_volume_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_volume_second.addItem("Κυβικό Μέτρο")
        self.button_volume_second.addItem("Κυβικό Εκατοστό")
        self.button_volume_second.addItem("Λίτρο")
        self.button_volume_second.addItem("Κυβικό Πόδι")
        self.button_volume_second.addItem("Κυβική Ίντσα")
        self.button_volume_second.addItem("Κυβική Γιάρδα")
        self.button_volume_second.setCurrentIndex(0)
        #       * Data buttons
        self.button_data_first = QComboBox()
        self.button_data_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_data_first.addItem('Bits')
        self.button_data_first.addItem('Bytes')
        self.button_data_first.addItem('KiloBytes')
        self.button_data_first.addItem('MegaBytes')
        self.button_data_first.addItem('GigaBytes')
        self.button_data_first.addItem('TeraBytes')
        self.button_data_first.addItem('PetaBytes')
        self.button_data_first.setCurrentIndex(0)

        self.button_data_second = QComboBox()
        self.button_data_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_data_second.addItem('Bits')
        self.button_data_second.addItem('Bytes')
        self.button_data_second.addItem('KiloBytes')
        self.button_data_second.addItem('MegaBytes')
        self.button_data_second.addItem('GigaBytes')
        self.button_data_second.addItem('TeraBytes')
        self.button_data_second.addItem('PetaBytes')
        self.button_data_second.setCurrentIndex(0)

        #       * Mass buttons
        self.button_mass_first = QComboBox()
        self.button_mass_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_mass_first.addItem('Κιλά')
        self.button_mass_first.addItem('Λίβρες')
        self.button_mass_first.addItem('Ουγγιά')
        self.button_mass_first.addItem('Καράτια')
        self.button_mass_first.addItem('Γραμμάρια')
        self.button_mass_first.setCurrentIndex(0)

        self.button_mass_second = QComboBox()
        self.button_mass_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_mass_second.addItem('Κιλά')
        self.button_mass_second.addItem('Λίβρες')
        self.button_mass_second.addItem('Ουγγιά')
        self.button_mass_second.addItem('Καράτια')
        self.button_mass_second.addItem('Γραμμάρια')
        self.button_mass_second.setCurrentIndex(0)

        #       * Speed buttons
        self.button_speed_first = QComboBox()
        self.button_speed_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_speed_first.addItem('Χιλιόμετρα/ώ')
        self.button_speed_first.addItem('Μίλια/ώ')
        self.button_speed_first.addItem('Μέτρα/δ')
        self.button_speed_first.addItem('Πόδια/δ')
        self.button_speed_first.addItem('Μάχ')
        self.button_speed_first.addItem('Κόμβοι')
        self.button_speed_first.setCurrentIndex(0)

        self.button_speed_second = QComboBox()
        self.button_speed_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_speed_second.addItem('Χιλιόμετρα/ώ')
        self.button_speed_second.addItem('Μίλια/ώ')
        self.button_speed_second.addItem('Μέτρα/δ')
        self.button_speed_second.addItem('Πόδια/δ')
        self.button_speed_second.addItem('Μάχ')
        self.button_speed_second.addItem('Κόμβοι')
        self.button_speed_second.setCurrentIndex(0)

        #       * Length buttons
        self.button_length_first = QComboBox()
        self.button_length_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_length_first.addItem('Μέτρα')
        self.button_length_first.addItem('Πόδια')
        self.button_length_first.addItem('Χιλιόμετρα')
        self.button_length_first.addItem('Μίλια')
        self.button_length_first.addItem('Ίντσες')
        self.button_length_first.addItem('Γιάρδες')
        self.button_length_first.addItem('Ναυτικά Μίλια')
        self.button_length_first.setCurrentIndex(0)

        self.button_length_second = QComboBox()
        self.button_length_second.setGeometry(QRect(10, 10, 10, 10))
        self.button_length_second.addItem('Μέτρα')
        self.button_length_second.addItem('Πόδια')
        self.button_length_second.addItem('Χιλιόμετρα')
        self.button_length_second.addItem('Μίλια')
        self.button_length_second.addItem('Ίντσες')
        self.button_length_second.addItem('Γιάρδες')
        self.button_length_second.addItem('Ναυτικά Μίλια')
        self.button_length_second.setCurrentIndex(0)

        #       * BMI buttons
        self.button_bmi_first = QComboBox()
        self.button_bmi_first.setGeometry(QRect(10, 10, 10, 10))
        self.button_bmi_first.addItem("Κιλά/Μέτρα")
        self.button_bmi_first.addItem("Λίβρες/Ίντσες")
        self.button_bmi_first.setCurrentIndex(0)
        # --------------------------

    #   FOR THE STANDARD AND SCIENTIFIC NUMBER BUTTONS
    def _QPushButton_button_nums(self, mode='standard'):
        # -- Local tuple attribute --
        button_values = ('7', '8', '9', '4', '5', '6', '1', '2', '3', '0')
        # ---------------------------

        # -- Assigning the correct pointer values based on the appropriate mode --
        k = 0
        if mode == 'scientific':
            k = 1
        j = 4 + (k * 2)
        i = 1 + k
        # ------------------------------------------------------------------------

        # -- Mass creating the number buttons and assigning them based on the calculator mode --
        for n, button_value in enumerate(button_values):
            # Creating the corresponding button number based on the 'button_values' tuple
            self.button_num = QPushButton(button_value, self)

            # Connecting to the appropriate 'button_num' function
            self.button_num.clicked.connect(self.button_num_caller(button_value))

            # Assigning the 'font_button' (QFont) to the 'QPushButton' attribute(s)
            self.button_num.setFont(self.font_button)

            # Assigning the 'SizePolicy' to the 'QPushButton' attribute(s)
            self.button_num.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

            # Handing the input/output based on the calculator mode
            if button_value != '0':
                if mode == 'scientific':
                    self.layout_grid_scientific.addWidget(self.button_num, j, i)
                else:
                    self.layout_grid_standard.addWidget(self.button_num, j, i)

                i = i + 1
                if i == 4 + k:
                    j = j + 1
                    i = 1 + k
            else:
                if mode == 'scientific':
                    self.layout_grid_scientific.addWidget(self.button_num, 9, 3)
                else:
                    self.layout_grid_standard.addWidget(self.button_num, 7, 2)
        # --------------------------------------------------------------------------------------

    #   FOR THE STANDARD CALCULATOR MODE
    def _QLineEdit_standard_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box.setReadOnly(True)
        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(250)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(250)
        self.symbol_box.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_standard_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """
        font_symbol = QFont()
        font_extra = QFont()

        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton attributes --
        #       * Number buttons
        """ The number buttons are already assigned in the '_QPushButton_button_nums' """

        #       * Operand buttons
        self.button_equal.setFont(font_symbol)
        self.button_plus.setFont(font_symbol)
        self.button_minus.setFont(font_symbol)
        self.button_times.setFont(font_symbol)
        self.button_division.setFont(font_symbol)

        #       * Symbol buttons
        self.button_clear_entry.setFont(font_extra)
        self.button_clear.setFont(font_extra)
        self.button_backspace.setFont(font_extra)
        self.button_inverse.setFont(font_extra)
        self.button_dot.setFont(font_symbol)
        # ------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton attributes --
        #       * Number buttons
        """ The number buttons are already assigned in the '_QPushButton_button_nums' """

        #       * Operand buttons
        self.button_equal.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_plus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_minus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_times.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_division.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #       * Symbol buttons
        self.button_clear_entry.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_clear.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_backspace.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_inverse.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_dot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_standard_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_standard.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_standard.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_standard(self):
        # -- Calculator Standard QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_standard.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_standard.addWidget(self.symbol_box, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_standard.addWidget(self.display_box, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_standard.addWidget(self.button_clear_entry, 3, 1)
        self.layout_grid_standard.addWidget(self.button_clear, 3, 2)
        self.layout_grid_standard.addWidget(self.button_backspace, 3, 3)
        self.layout_grid_standard.addWidget(self.button_division, 3, 4)

        #       Regards the fourth row of the grid
        """ The 7, 8, 9 are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_standard.addWidget(self.button_times, 4, 4)

        #       Regards the fifth row of the grid
        """ The 4, 5, 6 are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_standard.addWidget(self.button_minus, 5, 4)

        #       Regards the sixth row of the grid
        """ The 1, 2, 3are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_standard.addWidget(self.button_plus, 6, 4)

        #       Regards the seventh row of the grid
        self.layout_grid_standard.addWidget(self.button_inverse, 7, 1)
        """ The 0 is already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_standard.addWidget(self.button_dot, 7, 3)
        self.layout_grid_standard.addWidget(self.button_equal, 7, 4)
        # ------------------------------

    #   FOR THE SCIENTIFIC CALCULATOR MODE
    def _QLineEdit_scientific_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box.setReadOnly(True)
        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(250)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(250)
        self.symbol_box.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_scientific_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """
        font_symbol = QFont()
        font_extra = QFont()

        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)

        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton attributes --
        #       * Number buttons
        """ The number buttons are already assigned in the '_QPushButton_button_nums' """

        #       * Algebraic buttons
        self.button_exponent.setFont(font_extra)
        self.button_raise.setFont(font_extra)
        self.button_absolute.setFont(font_extra)
        self.button_sqrt.setFont(font_extra)
        self.button_log.setFont(font_extra)
        self.button_ln.setFont(font_extra)
        self.button_pi.setFont(font_extra)
        self.button_factorial.setFont(font_extra)

        #       * Trigonometric buttons
        self.button_sin.setFont(font_extra)
        self.button_cos.setFont(font_extra)
        self.button_tan.setFont(font_extra)

        #       * Operand buttons
        self.button_equal.setFont(font_symbol)
        self.button_plus.setFont(font_symbol)
        self.button_minus.setFont(font_symbol)
        self.button_times.setFont(font_symbol)
        self.button_division.setFont(font_symbol)
        self.button_modular.setFont(font_extra)
        self.button_percent.setFont(font_extra)

        #       * Symbol buttons
        self.button_clear_entry.setFont(font_extra)
        self.button_clear.setFont(font_extra)
        self.button_backspace.setFont(font_extra)
        self.button_inverse.setFont(font_extra)
        self.button_dot.setFont(font_symbol)
        self.button_left_bracket.setFont(font_extra)
        self.button_right_bracket.setFont(font_extra)
        # ------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton attributes --
        #       * Number buttons
        """ The number buttons are already assigned in the '_QPushButton_button_nums' """

        #       * Algebraic buttons
        self.button_exponent.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_raise.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_absolute.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_sqrt.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_log.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_ln.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_pi.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_factorial.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        #       * Trigonometric buttons
        self.button_sin.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_cos.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_tan.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        #       * Operand buttons
        self.button_equal.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_plus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_minus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_times.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_division.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_modular.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_percent.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        #       * Symbol buttons
        self.button_clear_entry.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_clear.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_backspace.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_inverse.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_dot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_left_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_right_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_scientific_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_scientific.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_scientific.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_scientific(self):
        # -- Calculator Scientific QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_scientific.addWidget(self.menu_bar, 0, 1, 1, 5)

        #       Regards the first row of the grid
        self.layout_grid_scientific.addWidget(self.symbol_box, 1, 1, 1, 5)

        #       Regards the second row of the grid
        self.layout_grid_scientific.addWidget(self.display_box, 2, 1, 1, 5)

        #       Regards the third row of the grid
        self.layout_grid_scientific.addWidget(self.button_exponent, 3, 1)
        self.layout_grid_scientific.addWidget(self.button_raise, 3, 2)
        self.layout_grid_scientific.addWidget(self.button_sin, 3, 3)
        self.layout_grid_scientific.addWidget(self.button_cos, 3, 4)
        self.layout_grid_scientific.addWidget(self.button_tan, 3, 5)

        #       Regards the fourth row of the grid
        self.layout_grid_scientific.addWidget(self.button_sqrt, 4, 1)
        self.layout_grid_scientific.addWidget(self.button_absolute, 4, 2)
        self.layout_grid_scientific.addWidget(self.button_log, 4, 3)
        self.layout_grid_scientific.addWidget(self.button_ln, 4, 4)
        self.layout_grid_scientific.addWidget(self.button_modular, 4, 5)

        #       Regards the fifth row of the grid
        self.layout_grid_scientific.addWidget(self.button_percent, 5, 1)
        self.layout_grid_scientific.addWidget(self.button_clear_entry, 5, 2)
        self.layout_grid_scientific.addWidget(self.button_clear, 5, 3)
        self.layout_grid_scientific.addWidget(self.button_backspace, 5, 4)
        self.layout_grid_scientific.addWidget(self.button_division, 5, 5)

        #       Regards the sixth row of the grid
        self.layout_grid_scientific.addWidget(self.button_pi, 6, 1)
        """ The 7, 8, 9 are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_scientific.addWidget(self.button_times, 6, 5)

        #       Regards the seventh row of the grid
        self.layout_grid_scientific.addWidget(self.button_factorial, 7, 1)
        """ The 4, 5, 6 are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_scientific.addWidget(self.button_minus, 7, 5)

        #       Regards the eighth row of the grid
        self.layout_grid_scientific.addWidget(self.button_inverse, 8, 1)
        """ The 1, 2, 3 are already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_scientific.addWidget(self.button_plus, 8, 5)

        #       Regards the ninth row of the grid
        self.layout_grid_scientific.addWidget(self.button_left_bracket, 9, 1)
        self.layout_grid_scientific.addWidget(self.button_right_bracket, 9, 2)
        """ The 0 is already declared in the '_QPushButton_button_nums' function """
        self.layout_grid_scientific.addWidget(self.button_dot, 9, 4)
        self.layout_grid_scientific.addWidget(self.button_equal, 9, 5)
        # ------------------------------

    #   FOR THE TEMPERATURE CALCULATOR MODE
    def _QLineEdit_temperature_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_temperature.setReadOnly(False)
        self.display_box_temperature.setAlignment(Qt.AlignRight)
        self.display_box_temperature.setMaxLength(250)
        self.display_box_temperature.setFont(font_display_box)

        self.symbol_box_temperature.setReadOnly(True)
        self.symbol_box_temperature.setAlignment(Qt.AlignRight)
        self.symbol_box_temperature.setMaxLength(250)
        self.symbol_box_temperature.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_temperature_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """
        font_symbol = QFont()
        font_extra = QFont()

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton attributes --
        #       * Temperature buttons
        self.button_temperature_calculate.setFont(self.font_button)
        # ------------------------------------------------------------------

        # -- Assigning our QFont attributes to our QComboBox attributes --
        #       * Temperature buttons
        self.button_temperature_first.setFont(self.font_button)
        self.button_temperature_second.setFont(self.font_button)
        # ----------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton attributes --
        #       * Temperature buttons
        self.button_temperature_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

        # -- Assigning a size policy to our QComboBox attributes --
        #       * Temperature buttons
        self.button_temperature_first.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_temperature_second.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # ---------------------------------------------------------

    def _QGridLayout_temperature_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_temperature.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_temperature.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_temperature(self):
        # -- Calculator Temperature QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_temperature.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_temperature.addWidget(self.display_box_temperature, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_temperature.addWidget(self.symbol_box_temperature, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_temperature.addWidget(self.button_temperature_first, 4, 1)
        self.layout_grid_temperature.addWidget(self.button_temperature_second, 4, 3)

        #       Regards the fifth row of the grid
        self.layout_grid_temperature.addWidget(self.button_temperature_calculate, 5, 2)
        # ----------------------------------------

    #   FOR THE TIME CALCULATOR MODE
    def _QLineEdit_time_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_time.setReadOnly(False)
        self.display_box_time.setAlignment(Qt.AlignRight)
        self.display_box_time.setMaxLength(250)
        self.display_box_time.setFont(font_display_box)

        self.symbol_box_time.setReadOnly(True)
        self.symbol_box_time.setAlignment(Qt.AlignRight)
        self.symbol_box_time.setMaxLength(250)
        self.symbol_box_time.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_time_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Time buttons
        self.button_time_calculate.setFont(self.font_button)

        self.button_time_first.setFont(self.font_button)
        self.button_time_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Time buttons
        self.button_time_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        self.button_time_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_time_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_time_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_time.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_time.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_time(self):
        # -- Calculator Time QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_time.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_time.addWidget(self.display_box_time, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_time.addWidget(self.symbol_box_time, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_time.addWidget(self.button_time_first, 4, 1)
        self.layout_grid_time.addWidget(self.button_time_second, 4, 3)

        #       Regards the fifth row of the grid
        self.layout_grid_time.addWidget(self.button_time_calculate, 5, 2)
        # ----------------------------------------

    #   FOR THE VOLUME CALCULATOR MODE
    def _QLineEdit_volume_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_volume.setReadOnly(False)
        self.display_box_volume.setAlignment(Qt.AlignRight)
        self.display_box_volume.setMaxLength(250)
        self.display_box_volume.setFont(font_display_box)

        self.symbol_box_volume.setReadOnly(True)
        self.symbol_box_volume.setAlignment(Qt.AlignRight)
        self.symbol_box_volume.setMaxLength(250)
        self.symbol_box_volume.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_volume_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Volume buttons
        self.button_volume_calculate.setFont(self.font_button)
        self.button_volume_first.setFont(self.font_button)
        self.button_volume_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Volume buttons
        self.button_volume_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_volume_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_volume_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_volume_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_volume.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_volume.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_volume(self):
        # -- Calculator Date QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_volume.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_volume.addWidget(self.display_box_volume, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_volume.addWidget(self.symbol_box_volume, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_volume.addWidget(self.button_volume_second, 3, 1)
        self.layout_grid_volume.addWidget(self.button_volume_first, 3, 3)

        #       Regards the fourth row of the grid
        self.layout_grid_volume.addWidget(self.button_volume_calculate, 4, 2)
        # ----------------------------------------

    #   FOR THE DATA CALCULATOR MODE
    def _QLineEdit_data_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_data.setReadOnly(False)
        self.display_box_data.setAlignment(Qt.AlignRight)
        self.display_box_data.setMaxLength(250)
        self.display_box_data.setFont(font_display_box)

        self.symbol_box_data.setReadOnly(True)
        self.symbol_box_data.setAlignment(Qt.AlignRight)
        self.symbol_box_data.setMaxLength(250)
        self.symbol_box_data.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_data_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Data buttons
        self.button_data_calculate.setFont(self.font_button)
        self.button_data_first.setFont(self.font_button)
        self.button_data_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Data buttons
        self.button_data_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_data_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_data_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_data_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_data.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_data.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_data(self):
        # -- Calculator Data QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_data.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_data.addWidget(self.display_box_data, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_data.addWidget(self.symbol_box_data, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_data.addWidget(self.button_data_second, 3, 1)
        self.layout_grid_data.addWidget(self.button_data_first, 3, 3)

        #       Regards the fourth row of the grid
        self.layout_grid_data.addWidget(self.button_data_calculate, 4, 2)
        # ----------------------------------------

    #   FOR THE DISCOUNT CALCULATOR MODE
    def _QLineEdit_discount_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 8)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_discount.setReadOnly(False)
        self.display_box_discount.setAlignment(Qt.AlignRight)
        self.display_box_discount.setMaxLength(250)
        self.display_box_discount.setFont(font_display_box)

        self.display_box_discount1.setReadOnly(False)
        self.display_box_discount1.setAlignment(Qt.AlignRight)
        self.display_box_discount1.setMaxLength(250)
        self.display_box_discount1.setFont(font_display_box)

        self.symbol_box_discount.setReadOnly(True)
        self.symbol_box_discount.setAlignment(Qt.AlignRight)
        self.symbol_box_discount.setMaxLength(250)
        self.symbol_box_discount.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_discount_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Discount buttons
        self.button_discount_calculate.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Discount buttons
        self.button_discount_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_discount_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_discount.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_discount.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_discount(self):
        # -- Calculator Discount QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_discount.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_discount.addWidget(self.display_box_discount, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_discount.addWidget(self.display_box_discount1, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_discount.addWidget(self.button_discount_calculate, 3, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_discount.addWidget(self.symbol_box_discount, 4, 1, 1, 4)
        # ----------------------------------------

    #   FOR THE AGE CALCULATOR MODE
    def _QLineEdit_age_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_display_box_extra = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 5)
        font_display_box_extra.setPointSize(font_display_box_extra.pointSize() + 2)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize())
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.symbol_box_age.setReadOnly(False)
        self.symbol_box_age.setAlignment(Qt.AlignRight)
        self.symbol_box_age.setMaxLength(250)
        self.symbol_box_age.setFont(font_display_box)
        # -------------------------------------------------------------

    def _QPushButton_age_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Age buttons
        self.button_age_calculate.setFont(self.font_button)
        self.button_age_clear.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Age buttons
        self.button_age_calculate.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_age_clear.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_age_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_age.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_age.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_age(self):
        # -- Calculator Age QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_age.addWidget(self.menu_bar, 0, 1, 1, 4)

        self.layout_grid_age.addWidget(self.symbol_box_age, 1, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_age.addWidget(self.button_age_clear, 3, 1)
        self.layout_grid_age.addWidget(self.button_age_calculate, 3, 2)

        #       Regards the fourth row of the grid
        # ----------------------------------------

    #   FOR THE MASS CALCULATOR MODE
    def _QLineEdit_mass_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_mass.setReadOnly(False)
        self.display_box_mass.setAlignment(Qt.AlignRight)
        self.display_box_mass.setMaxLength(250)
        self.display_box_mass.setFont(font_display_box)

        self.symbol_box_mass.setReadOnly(True)
        self.symbol_box_mass.setAlignment(Qt.AlignRight)
        self.symbol_box_mass.setMaxLength(250)
        self.symbol_box_mass.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_mass_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Mass buttons
        self.button_mass_calculate.setFont(self.font_button)
        self.button_mass_first.setFont(self.font_button)
        self.button_mass_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Mass buttons
        self.button_mass_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_mass_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_mass_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_mass_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_mass.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_mass.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_mass(self):
        # -- Calculator Mass QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_mass.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_mass.addWidget(self.display_box_mass, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_mass.addWidget(self.symbol_box_mass, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_mass.addWidget(self.button_mass_second, 3, 1)
        self.layout_grid_mass.addWidget(self.button_mass_first, 3, 3)

        #       Regards the fourth row of the grid
        self.layout_grid_mass.addWidget(self.button_mass_calculate, 4, 2)
        # ----------------------------------------

    #   FOR THE SPEED CALCULATOR MODE
    def _QLineEdit_speed_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_speed.setReadOnly(False)
        self.display_box_speed.setAlignment(Qt.AlignRight)
        self.display_box_speed.setMaxLength(250)
        self.display_box_speed.setFont(font_display_box)

        self.symbol_box_speed.setReadOnly(True)
        self.symbol_box_speed.setAlignment(Qt.AlignRight)
        self.symbol_box_speed.setMaxLength(250)
        self.symbol_box_speed.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_speed_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Speed buttons
        self.button_speed_calculate.setFont(self.font_button)
        self.button_speed_first.setFont(self.font_button)
        self.button_speed_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Speed buttons
        self.button_speed_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_speed_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_speed_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_speed_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_speed.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_speed.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_speed(self):
        # -- Calculator Speed QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout

        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_speed.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_speed.addWidget(self.display_box_speed, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_speed.addWidget(self.symbol_box_speed, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_speed.addWidget(self.button_speed_second, 3, 1)
        self.layout_grid_speed.addWidget(self.button_speed_first, 3, 3)

        #       Regards the fourth row of the grid
        self.layout_grid_speed.addWidget(self.button_speed_calculate, 4, 2)
        # ----------------------------------------

    #   FOR THE LENGTH CALCULATOR MODE
    def _QLineEdit_length_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_length.setReadOnly(False)
        self.display_box_length.setAlignment(Qt.AlignRight)
        self.display_box_length.setMaxLength(250)
        self.display_box_length.setFont(font_display_box)

        self.symbol_box_length.setReadOnly(True)
        self.symbol_box_length.setAlignment(Qt.AlignRight)
        self.symbol_box_length.setMaxLength(250)
        self.symbol_box_length.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_length_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * Length buttons
        self.button_length_calculate.setFont(self.font_button)
        self.button_length_first.setFont(self.font_button)
        self.button_length_second.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * Length buttons
        self.button_length_calculate.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_length_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_length_second.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_length_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_length.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_length.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_length(self):
        # -- Calculator Length QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_length.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_length.addWidget(self.display_box_length, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_length.addWidget(self.symbol_box_length, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_length.addWidget(self.button_length_second, 3, 1)
        self.layout_grid_length.addWidget(self.button_length_first, 3, 3)

        #       Regards the fourth row of the grid
        self.layout_grid_length.addWidget(self.button_length_calculate, 4, 2)
        # ----------------------------------------

    #   FOR THE BMI CALCULATOR MODE
    def _QLineEdit_bmi_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box_bmi.setReadOnly(False)
        self.display_box_bmi.setAlignment(Qt.AlignRight)
        self.display_box_bmi.setMaxLength(250)
        self.display_box_bmi.setFont(font_display_box)

        self.display_box_bmi1.setReadOnly(False)
        self.display_box_bmi1.setAlignment(Qt.AlignRight)
        self.display_box_bmi1.setMaxLength(250)
        self.display_box_bmi1.setFont(font_display_box)

        self.symbol_box_bmi.setReadOnly(True)
        self.symbol_box_bmi.setAlignment(Qt.AlignRight)
        self.symbol_box_bmi.setMaxLength(250)
        self.symbol_box_bmi.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_bmi_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's & QComboBox's attributes font
        """ self.font_button is already declared in the '_calculator_modes_declarations' """

        # For the QPushButton & QComboBox 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # -------------------------------------------------------

        # -- Assigning our QFont attributes to our QPushButton & QComboBox attributes --
        #       * BMI buttons
        self.button_bmi_calculate.setFont(self.font_button)
        self.button_bmi_first.setFont(self.font_button)
        # ------------------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton & QComboBox attributes --
        #       * BMI buttons
        self.button_bmi_calculate.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_bmi_first.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------------------

    def _QGridLayout_bmi_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_bmi.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_bmi.setSpacing(1.8)
        # --------------------------------------------

    def _QGridLayout_bmi(self):
        # -- Calculator BMI QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout

        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_bmi.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_bmi.addWidget(self.display_box_bmi, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_bmi.addWidget(self.display_box_bmi1, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_bmi.addWidget(self.button_bmi_first, 3, 1)
        self.layout_grid_bmi.addWidget(self.button_bmi_calculate, 3, 2)

        #       Regards the fourth row of the grid
        self.layout_grid_bmi.addWidget(self.symbol_box_bmi, 4, 1, 1, 4)

        # ----------------------------------------

    # ** LAYOUT MODES **
    def _QWidget_calculator_standard(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_standard = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_standard_properties()
        # --------------------------

        # -- QPushButton properties --
        self._QPushButton_standard_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE STANDARD CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_standard = QGridLayout()
        self._QPushButton_button_nums(mode='standard')
        self._QGridLayout_standard_properties()
        self._QGridLayout_standard()

        self.widget_calculator_standard.setLayout(self.layout_grid_standard)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_standard)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_scientific(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_scientific = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_scientific_properties()
        # --------------------------

        # -- QPushButton properties --
        self._QPushButton_scientific_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_scientific = QGridLayout()
        self._QPushButton_button_nums(mode='scientific')
        self._QGridLayout_scientific_properties()
        self._QGridLayout_scientific()

        self.widget_calculator_scientific.setLayout(self.layout_grid_scientific)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_scientific)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_temperature(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_temperature = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_temperature_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_temperature_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_temperature = QGridLayout()
        self._QGridLayout_temperature_properties()
        self._QGridLayout_temperature()

        self.widget_calculator_temperature.setLayout(self.layout_grid_temperature)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_temperature)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_time(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_time = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_time_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_time_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_time = QGridLayout()
        self._QGridLayout_time_properties()
        self._QGridLayout_time()

        self.widget_calculator_time.setLayout(self.layout_grid_time)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_time)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_volume(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_volume = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_volume_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_volume_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_volume = QGridLayout()
        self._QGridLayout_volume_properties()
        self._QGridLayout_volume()

        self.widget_calculator_volume.setLayout(self.layout_grid_volume)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_volume)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_data(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_data = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_data_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_data_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_data = QGridLayout()
        self._QGridLayout_data_properties()
        self._QGridLayout_data()

        self.widget_calculator_data.setLayout(self.layout_grid_data)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_data)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_discount(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_discount = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_discount_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_discount_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_discount = QGridLayout()
        self._QGridLayout_discount_properties()
        self._QGridLayout_discount()

        self.widget_calculator_discount.setLayout(self.layout_grid_discount)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_discount)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_age(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_age = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_age_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_age_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_age = QGridLayout()
        self._QGridLayout_age_properties()
        self._QGridLayout_age()

        self.widget_calculator_age.setLayout(self.layout_grid_age)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_age)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_mass(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_mass = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_mass_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_mass_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_mass = QGridLayout()
        self._QGridLayout_mass_properties()
        self._QGridLayout_mass()

        self.widget_calculator_mass.setLayout(self.layout_grid_mass)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_mass)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_speed(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_speed = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_speed_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_speed_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_speed = QGridLayout()
        self._QGridLayout_speed_properties()
        self._QGridLayout_speed()

        self.widget_calculator_speed.setLayout(self.layout_grid_speed)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_speed)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_length(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_length = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_length_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_length_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_length = QGridLayout()
        self._QGridLayout_length_properties()
        self._QGridLayout_length()

        self.widget_calculator_length.setLayout(self.layout_grid_length)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_length)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_calculator_bmi(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_bmi = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_bmi_properties()
        # --------------------------

        # -- QPushButton & QComboBox properties --
        self._QPushButton_bmi_properties()
        # ----------------------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar properties --
        self._QMenuBar_properties()
        # -------------------------

        # -- QGridLayout --
        self.layout_grid_bmi = QGridLayout()
        self._QGridLayout_bmi_properties()
        self._QGridLayout_bmi()

        self.widget_calculator_bmi.setLayout(self.layout_grid_bmi)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_bmi)
        # ------------------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_global_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_global_signals()
        # -------------------------

    def _QWidget_mode_change(self):
        # QWidget.setGeometry(self, 450, 210, 370, 310)
        self.widget_Mode = QWidget()
        self.layout_grid_Mode = QGridLayout()
        self.menu_bar = QMenuBar()
        self.font_button = QFont()

        self._QMenuBar_properties()

        #       * Modes buttons
        self.button_STANDARD = QPushButton(QIcon('assets/calc.png'), "ΚΑΝΟΝΙΚΟ")
        self.button_SCIENTIFIC = QPushButton("ΕΠΙΣΤΗΜΟΝΙΚΟ")
        self.button_BMI = QPushButton(QIcon('assets/bmi.png'), "ΔΜΣ")
        self.button_AGE = QPushButton(QIcon('assets/age.png'), "ΗΛΙΚΙΑ")
        self.button_TIME = QPushButton(QIcon('assets/clock.png'), "ΧΡΟΝΟΣ")
        self.button_VOLUME = QPushButton(QIcon('assets/date.png'), "ΟΓΚΟΣ")
        self.button_DATA = QPushButton(QIcon('assets/data.png'), "ΔΕΔΟΜΕΝΑ")
        self.button_DISCOUNT = QPushButton(QIcon('assets/discount.png'), "ΕΚΠΤΩΣΗ")
        self.button_LENGTH = QPushButton(QIcon('assets/length.png'), "ΜΗΚΟΣ")
        self.button_MASS = QPushButton(QIcon('assets/mass.png'), "ΜΑΖΑ")
        self.button_SPEED = QPushButton(QIcon('assets/speed.png'), "ΤΑΧΥΤΗΤΑ")
        self.button_TEMPERATURE = QPushButton(QIcon('assets/temperature.png'), "ΘΕΡΜΟΚΡΑΣΙΑ")

        self.font_button.setPointSize(self.font_button.pointSize() + 6)

        #       * Modes buttons
        self.button_STANDARD.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SCIENTIFIC.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_BMI.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_AGE.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_DATA.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_VOLUME.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_TIME.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SPEED.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_DISCOUNT.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_LENGTH.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_MASS.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_TEMPERATURE.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_Mode.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_Mode.addWidget(self.button_STANDARD, 1, 1, 1, 1)
        self.layout_grid_Mode.addWidget(self.button_SCIENTIFIC, 1, 2, 1, 1)
        self.layout_grid_Mode.addWidget(self.button_DISCOUNT, 1, 3, 1, 1)

        #       Regards the fifth row of the grid
        self.layout_grid_Mode.addWidget(self.button_DATA, 2, 1)
        self.layout_grid_Mode.addWidget(self.button_VOLUME, 2, 2)
        self.layout_grid_Mode.addWidget(self.button_BMI, 2, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_Mode.addWidget(self.button_TIME, 3, 1)
        self.layout_grid_Mode.addWidget(self.button_MASS, 3, 2)
        self.layout_grid_Mode.addWidget(self.button_LENGTH, 3, 3)

        #       Regards the seventh row of the grid
        self.layout_grid_Mode.addWidget(self.button_SPEED, 4, 1)
        self.layout_grid_Mode.addWidget(self.button_AGE, 4, 2)
        self.layout_grid_Mode.addWidget(self.button_TEMPERATURE, 4, 3)

        #       * Modes button signals/events
        self.button_STANDARD.clicked.connect(self.pressed_STANDARD)
        self.button_BMI.clicked.connect(self.pressed_BMI)
        self.button_DISCOUNT.clicked.connect(self.pressed_DISCOUNT)
        self.button_LENGTH.clicked.connect(self.pressed_LENGTH)
        self.button_MASS.clicked.connect(self.pressed_MASS)
        self.button_AGE.clicked.connect(self.pressed_AGE)
        self.button_TEMPERATURE.clicked.connect(self.pressed_TEMPERATURE)
        self.button_DATA.clicked.connect(self.pressed_DATA)
        self.button_SPEED.clicked.connect(self.pressed_SPEED)
        self.button_TIME.clicked.connect(self.pressed_TIME)
        self.button_VOLUME.clicked.connect(self.pressed_VOLUME)
        self.button_SCIENTIFIC.clicked.connect(self.pressed_SCIENTIFIC)

        self.layout_grid_Mode.setContentsMargins(10, 12, 4, 10)
        self.layout_grid_Mode.setSpacing(6)
        self._QMenuBar_global_signals()

        self.widget_Mode.setLayout(self.layout_grid_Mode)
        QMainWindow.setCentralWidget(self, self.widget_Mode)

    def _QWidget_theme_change(self):
        self.widget_Theme = QWidget()
        self.layout_grid_Theme = QGridLayout()
        self.menu_bar = QMenuBar()
        self.font_button = QFont()
        self.font_test_display_box = QFont()

        self._QMenuBar_properties()

        self.test_display_box_1 = QLineEdit('Έτσι θα φαίνεται το κείμενο')
        self.test_display_box_2 = QLineEdit(
            'Επιλέξτε αυτό το κείμενο για να δείτε πως θα φαίνεται το επισημασμένο κέιμενο')

        self.test_display_box_1.setReadOnly(True)
        self.test_display_box_2.setReadOnly(True)
        self.test_display_box_2.selectAll()

        self.button_background_color = QPushButton('Χρώμα Φόντου')
        self.button_text_color = QPushButton('Χρώμα Κειμένου')
        self.button_button_color = QPushButton('Χρώμα Φόντου Κουμπιών')
        self.button_display_color = QPushButton('Χρώμα Οθόνης')
        self.button_display_text = QPushButton('Χρώμα Κειμένου Οθόνης')
        self.button_reset_white_colors = QPushButton('Επαναφορά Λευκού Θέματος')
        self.button_reset_dark_colors = QPushButton('Επαναφορά Σκωτεινού Θέματος')

        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        self.font_test_display_box.setPointSize(self.font_test_display_box.pointSize() + 10)

        self.test_display_box_1.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.test_display_box_2.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_background_color.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_text_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_button_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_display_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_display_text.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_reset_white_colors.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_reset_dark_colors.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        self.layout_grid_Theme.addWidget(self.menu_bar, 0, 0, 1, 4)
        self.layout_grid_Theme.addWidget(self.test_display_box_1, 1, 0, 1, 4)
        self.layout_grid_Theme.addWidget(self.test_display_box_2, 2, 0, 1, 4)
        self.layout_grid_Theme.addWidget(self.button_background_color, 3, 0)
        self.layout_grid_Theme.addWidget(self.button_text_color, 3, 1)
        self.layout_grid_Theme.addWidget(self.button_button_color, 3, 2)
        self.layout_grid_Theme.addWidget(self.button_display_color, 3, 3)
        self.layout_grid_Theme.addWidget(self.button_display_text, 4, 0)
        self.layout_grid_Theme.addWidget(self.button_reset_dark_colors, 4, 1, 1, 2)
        self.layout_grid_Theme.addWidget(self.button_reset_white_colors, 4, 3, 1, 1)

        self.button_background_color.clicked.connect(self.pressed_button_background_color)
        self.button_text_color.clicked.connect(self.pressed_button_text_color)
        self.button_button_color.clicked.connect(self.pressed_button_color)
        self.button_display_color.clicked.connect(self.pressed_button_display_color)
        self.button_display_text.clicked.connect(self.pressed_button_display_text)
        self.button_reset_white_colors.clicked.connect(self._light_mode)
        self.button_reset_dark_colors.clicked.connect(self._dark_mode)

        self.layout_grid_Theme.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_Theme.setSpacing(10)

        self._QMenuBar_global_signals()

        self.widget_Theme.setLayout(self.layout_grid_Theme)
        QMainWindow.setCentralWidget(self, self.widget_Theme)

    # ** GLOBAL CLASS SIGNALS & EVENTS **
    def _QMenuBar_global_signals(self):
        # -- Calling our corresponding signal functions --
        #       Regards the 'self.menu_options' attribute
        self.menu_options_modes_act.triggered.connect(self._QWidget_mode_change)

        #       Regards the 'self.menu_settings' attribute
        self.menu_settings_themes_act.triggered.connect(self._QWidget_theme_change)

        #       Regards the 'self.menu_help' attribute
        self.menu_help_about_act.triggered.connect(self.clicked_help_about)
        # ------------------------------------------------

    def _QPushButton_global_signals(self):
        # -- Calling our corresponding signal functions --
        #       * Number button signals/events
        """ Already declared in the '_QPushButton_button_nums' function """

        #       * Algebraic buttons signals/events
        self.button_exponent.clicked.connect(self.pressed_button_exponent)
        self.button_raise.clicked.connect(self.pressed_button_raise)
        self.button_absolute.clicked.connect(self.pressed_button_absolute)
        self.button_sqrt.clicked.connect(self.pressed_button_sqrt)
        self.button_log.clicked.connect(self.pressed_button_log)
        self.button_ln.clicked.connect(self.pressed_button_ln)
        self.button_pi.clicked.connect(self.pressed_button_pi)
        self.button_factorial.clicked.connect(self.pressed_button_e)

        #       * Trigonometric buttons signals/events
        self.button_sin.clicked.connect(self.pressed_button_sin)
        self.button_cos.clicked.connect(self.pressed_button_cos)
        self.button_tan.clicked.connect(self.pressed_button_tan)

        #       * Operand button signals/events
        self.button_equal.clicked.connect(self.pressed_button_equal)
        self.button_plus.clicked.connect(self.pressed_button_plus)
        self.button_minus.clicked.connect(self.pressed_button_minus)
        self.button_times.clicked.connect(self.pressed_button_times)
        self.button_division.clicked.connect(self.pressed_button_division)
        self.button_modular.clicked.connect(self.pressed_button_modular)
        self.button_percent.clicked.connect(self.pressed_button_percent)

        #       * Symbol button signals/events
        self.button_clear_entry.clicked.connect(self.pressed_button_clear_entry)
        self.button_clear.clicked.connect(self.pressed_button_clear)
        self.button_backspace.clicked.connect(self.pressed_button_backspace)
        self.button_inverse.clicked.connect(self.pressed_button_inverse)
        self.button_dot.clicked.connect(self.pressed_button_dot)
        self.button_left_bracket.clicked.connect(self.pressed_button_left_bracket)
        self.button_right_bracket.clicked.connect(self.pressed_button_right_bracket)

        #       * Temperature button signals/events
        self.button_temperature_calculate.clicked.connect(self.pressed_button_temperature_calculate)

        #       * Time button signals/events
        self.button_time_calculate.clicked.connect(self.pressed_button_time_calculate)

        #       * Volume button signals/events
        self.button_volume_calculate.clicked.connect(self.pressed_button_volume_calculate)

        #       * Data button signals/events
        self.button_data_calculate.clicked.connect(self.pressed_button_data_calculate)

        #       * Discount button signals/events
        self.button_discount_calculate.clicked.connect(self.pressed_button_discount_calculate)

        #       * Age button signals/events
        self.button_age_calculate.clicked.connect(self.pressed_button_age_calculate)
        self.button_age_clear.clicked.connect(self.pressed_button_age_clear)

        #       * Mass button signals/events
        self.button_mass_calculate.clicked.connect(self.pressed_button_mass_calculate)

        #       * Speed button signals/events
        self.button_speed_calculate.clicked.connect(self.pressed_button_speed_calculate)

        #       * Length button signals/events
        self.button_length_calculate.clicked.connect(self.pressed_button_length_calculate)

        #       * BMI button signals/events
        self.button_bmi_calculate.clicked.connect(self.pressed_button_bmi_calculate)
        # ------------------------------------------------

    def _QMenuBar_properties(self):
        # -- Assigning our attributes to the QMenuBar --
        self.menu_options = self.menu_bar.addMenu('Επιλογές')
        self.menu_settings = self.menu_bar.addMenu('Ρυθμίσεις')
        self.menu_help = self.menu_bar.addMenu('Βοήθεια')
        # ----------------------------------------------

        # -- Creating QAction attributes and connecting them to the menu attributes
        #       Regards the 'self.menu_options' attribute
        self.menu_options_overhead_name = QAction('Λειτουργίες Αριθμομηχανής')
        self.menu_options_overhead_name.setSeparator(True)

        self.menu_options_modes_act = QAction('Λειτουργίες')
        self.menu_options_modes_act.setShortcut('Ctrl+M')
        self.menu_options_modes_act.setChecked(True)

        #       Regards the 'self.menu_settings' attribute
        self.menu_settings_themes_act = QAction('Θέματα')
        self.menu_settings_themes_act.setShortcut('Ctrl+T')
        self.menu_settings_themes_act.setChecked(True)

        #       Regards the 'self.menu_help' attribute
        self.menu_help_about_act = QAction('Σχετικά με την εφαρμογή')
        self.menu_help_about_act.setChecked(True)
        # -------------------------------------------------------------------------

        # -- Assigning our QActions to the corresponding 'QMenuBar' attributes
        #       Regards the 'self.menu_options' attribute
        self.menu_options.addAction(self.menu_options_overhead_name)
        self.menu_options.addAction(self.menu_options_modes_act)

        #       Regards the 'self.menu_settings' attribute
        self.menu_settings.addAction(self.menu_settings_themes_act)

        #       Regards the 'self.menu_help' attribute
        self.menu_help.addAction(self.menu_help_about_act)
        # --------------------------------------------------------------------

    def _dark_mode(self):
        # -- Creating and setting the properties for the Color Palettee
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.WindowText, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------

    def _light_mode(self):
        # -- Creating and setting the properties for the light mode Palette
        self.palette = QPalette()
        self.setPalette(self.palette)
        # -------------------------------------------------------------

    # ** CALCULATOR FUNCTIONS **
    def _calculate_invoked(self, function_called):
        # -- Displaying to the console --
        # print("calculate has been invoked from", function_called)
        # -------------------------------

        # -- Making the necessary assignments --
        # Handling them locally so as to not affect any of the 'self' attributes
        local_string_last_number_used = self.string_last_number_used
        local_string_symbol_box = self.string_symbol_box
        if local_string_last_number_used == local_string_symbol_box:
            return local_string_last_number_used
        else:
            return local_string_symbol_box
        # --------------------------------------

    def _update_string_attributes(self, symbol):
        # To be used inside symbol function (except equal) signals/events
        self.string_last_operand_used = symbol
        self.string_display_box = self.display_box.text()
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
        self.string_symbol_box = self.symbol_box.text()
        self.string_result += self.string_symbol_box + self.string_symbol_box

        # In special cases such as 'Mod', '√' and so on
        if symbol == 'Mod':
            self.string_last_number_used = '%'
        elif symbol == '√':
            self.string_last_number_used = '√'

    def _reset_symbol_flags(self, flag=False):
        # -- Resetting all of our flags --
        # Set to 'False' by default
        self.bool_plus_last_pressed = flag
        self.bool_minus_last_pressed = flag
        self.bool_times_last_pressed = flag
        self.bool_division_last_pressed = flag
        self.bool_modular_last_pressed = flag
        # --------------------------------

    def __init__(self):
        super().__init__()

        # -- QWidget's properties --
        self._QMainWindow_properties()
        # --------------------------

        # -- Temporary boolean attribute --
        self.bool_temp_modes = True
        self.bool_temp_color_scheme = True
        # ---------------------------------
        # -- Standard calculator --
        # To start the application with the standard calculator in place
        self._QWidget_calculator_standard()
        # -------------------------

        self._dark_mode()

    @Slot()
    # -- Slots & signals functions --
    # ** NUMBER BUTTONS SIGNALS **
    def button_num_caller(self, number_value):
        # Creating our inner function to handle the input/output of the appropriate number button
        def pressed_numX():
            # -- Displaying to the console --
            # print(number_value, 'has been pressed')
            # -------------------------------

            # -- If 0 is already on the 'display_box' return --
            if self.display_box.text() == '0':
                return
            # -------------------------------------------------

            # -- If equal was last called, clear the 'display_box'
            if self.bool_equal_last_pressed:
                self.display_box.clear()
                self.string_last_number_used = ''
                self.bool_equal_last_pressed = False
            # ---------------------------------------------------

            # -- Handing the input/output for the UI --
            # If another operand has not been pressed
            if self.bool_waiting_for_operand:
                self.display_box.setText(self.display_box.text() + number_value)
            # Else clear the 'display_box' and add 'number_value' to it
            else:
                self.display_box.clear()
                self.display_box.setText(self.display_box.text() + number_value)

            # Updating our string attribute(s)
            self.string_display_box = self.display_box.text()
            self.string_last_number_used += number_value

            # Resetting the operand flag(s)
            self.bool_waiting_for_operand = True
            # -----------------------------------------

        return pressed_numX

    # ** ALGEBRAIC BUTTONS SIGNALS **
    def pressed_button_exponent(self):
        # -- Displaying to the console --
        # print('x² has been pressed')
        # -------------------------------

        # Makes sure there is a number in the 'display_box'
        if self.display_box.text() != '' and not self.bool_bracket:
            self.symbol_box.clear()
            self.display_box.setText(self.display_box.text() + '**2')

        # Setting the '=' flag to false
        if self.bool_equal_last_pressed:
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

    def pressed_button_raise(self):
        # -- Displaying to the console --
        # print('xⁿ has been pressed')
        # -------------------------------

        # Makes sure there is a number in the 'display_box'
        if self.display_box.text() != '' and not self.bool_bracket:
            self.symbol_box.clear()
            self.display_box.setText(self.display_box.text() + '**')
            self.bool_bracket = True

        # Setting the '=' flag to false
        if self.bool_equal_last_pressed:
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

    def pressed_button_absolute(self):
        # -- Displaying to the console --
        # print('|x| has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'abs('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_sqrt(self):
        # -- Displaying to the console --
        # print('√ has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'sqrt('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_log(self):
        # -- Displaying to the console --
        # print('log has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'log10('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_ln(self):
        # -- Displaying to the console --
        # print('ln has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'log('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_pi(self):
        # -- Displaying to the console --
        # print('π has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.display_box.clear()

            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- prevents the ( from being deleted --
        st = ''
        keep = False
        for i in self.display_box.text():
            st += i
            if i == '(':
                keep = True
                break
        # If there is no ( in the 'display_box' sets the string to be empty
        if not keep:
            st = ''

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed clear the display
        if self.bool_waiting_for_operand:
            self.display_box.clear()

        self.display_box.setText(st + str(math.pi))

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += str(math.pi)

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_button_e(self):
        # -- Displaying to the console --
        print('e has been pressed')
        # -------------------------------
        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.string_last_number_used = ''
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- prevents the ( from being deleted --
        st = ''
        keep = False
        for i in self.display_box.text():
            st += i
            if i == '(':
                keep = True
                break
        # If there is no ( in the 'display_box' sets the string to be empty
        if not keep:
            st = ''

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed clear the display
        if self.bool_waiting_for_operand:
            self.display_box.clear()

        self.display_box.setText(st + str(math.e))

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += str(math.e)

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    # ** TRIGONOMETRIC BUTTON SIGNALS **
    def pressed_button_sin(self):
        # -- Displaying to the console --
        # print('sin has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'sin('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_cos(self):
        # -- Displaying to the console --
        # print('cos has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'cos('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    def pressed_button_tan(self):
        # -- Displaying to the console --
        # print('tan has been pressed')
        # -------------------------------

        # If '=' was last pressed clear the symbol box
        if self.bool_equal_last_pressed:
            self.string_last_number_used = ''
            self.symbol_box.clear()

        # -- Handing the input for the UI --
        self.string_symbol_box = 'tan('

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        # Makes sure you cant use ** next
        self.bool_bracket = False

        # Setting the waiting for operand to true
        self.bool_waiting_for_operand = True

        # Increases left bracket count
        self.left_bracket_count += 1

    # ** OPERAND BUTTONS SIGNALS **
    def pressed_button_equal(self):
        # -- Displaying to the console --
        # print('= has been pressed')
        # -------------------------------

        # If there is nothing in the display box then nothing happens
        if self.display_box.text() == '':
            return

        # Adds at the end of the string ) automatically
        add_brackets = self.left_bracket_count - self.right_bracket_count

        for i in range(add_brackets):
            self.display_box.setText(self.display_box.text() + ')')
        # ------------------------------

        # Resets the bracket count
        self.left_bracket_count = 0
        self.right_bracket_count = 0
        # ------------------------

        # -- If the last operand called was '=' calculate and return --
        if self.bool_equal_last_pressed:
            # Calculating the result and assigning it to the 'string_result' attribute
            self.string_result += self.string_last_operand_used + self.string_last_number_used

            # Clearing the contents of the 'string_symbol_box' and 'symbol_box' attributes
            self.string_symbol_box = ''  # Will use a 'string_history_box' later to hold it in
            self.symbol_box.clear()

            # Displaying the result to the 'display_box' attribute and return
            self.display_box.setText(str(ne.evaluate(str(self.string_result))))
            return
        # -------------------------------------------------------------

        # -- Updating our string attributes --
        self.string_display_box = self.display_box.text()
        self.string_symbol_box = self.symbol_box.text()
        self.string_result = self.string_symbol_box + self.string_display_box
        # ------------------------------------

        # -- Handing the input/output for the UI --
        # Displaying the result to the 'display_box' and clear the 'symbol_box'
        self.symbol_box.setText(self.string_result)

        self.display_box.setText(str(ne.evaluate(self.string_result)))

        # Clearing the 'string_symbol_box'attribute
        self.string_symbol_box = ''

        # Resetting the operand flag(s)
        self._reset_symbol_flags()
        self.bool_waiting_for_operand = True
        self.bool_equal_last_pressed = True
        # -----------------------------------------

    def pressed_button_plus(self):
        # -- Displaying to the console --
        # print('+ has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '+') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '+':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '+' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '+')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Adds at the end of the string ) automatically
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # --------------------------------

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()
            # Clearing the 'display_box' in the process
            self.display_box.clear()
            # Setting in the 'display_box' the overall result of the expression
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('+')))))

            # Removes the brackets from the symbol box for the next calculation to be added
            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '+')

            # Updating the string attribute(s)
            self.string_last_operand_used = '+'

            self._update_string_attributes('+')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()

            self.bool_waiting_for_operand = False

            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    def pressed_button_minus(self):
        # -- Displaying to the console --
        # print('- has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '-') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '-':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '-' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '-')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Adds at the end of the string ) automatically
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # --------------------------------

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()
            # Clearing the 'display_box' in the process
            self.display_box.clear()
            # Setting in the 'display_box' the overall result of the expression
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('-')))))

            # Removes the brackets from the symbol box for the next calculation to be added
            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '-')

            # Updating the string attribute(s)
            self.string_last_operand_used = '-'
            self._update_string_attributes('-')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    def pressed_button_times(self):
        # -- Displaying to the console --
        # print('* has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '*') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '*':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '*' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '*')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Adds at the end of the string ) automatically
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # --------------------------------

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()
            # Clearing the 'display_box' in the process
            self.display_box.clear()
            # Setting in the 'display_box' the overall result of the expression
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('*')))))

            # Removes the brackets from the symbol box for the next calculation to be added
            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '*')

            # Updating the string attribute(s)
            self.string_last_operand_used = '*'
            self._update_string_attributes('*')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    def pressed_button_division(self):
        # -- Displaying to the console --
        # print('/ has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if self.display_box.text() == '' or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '/') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '/':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '/' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '/')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Adds at the end of the string ) automatically
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # --------------------------------

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Setting in the 'display_box' the overall result of the expression
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('/')))))

            # Removes the brackets from the symbol box for the next calculation to be added
            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '/')

            # Updating the string attribute(s)
            self.string_last_operand_used = '/'

            self._update_string_attributes('/')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()

            self.bool_waiting_for_operand = False

            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '/') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '/':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '/' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '/')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Adds at the end of the string ) automatically
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # --------------------------------

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Setting in the 'display_box' the overall result of the expression
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('/')))))

            # Removes the brackets from the symbol box for the next calculation to be added
            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '/')

            # Updating the string attribute(s)
            self.string_last_operand_used = '/'

            self._update_string_attributes('/')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()

            self.bool_waiting_for_operand = False

            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    def pressed_button_modular(self):
        # -- Displaying to the console --
        # print('% has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '%') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '%':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '%' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '%')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('%')))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '%')

            # Updating the string attribute(s)
            self.string_last_operand_used = '%'
            self._update_string_attributes('%')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    def pressed_button_percent(self):
        # -- Displaying to the console --
        # print('% has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '%') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '%':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '%' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '%')
                return
        # ---------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')

            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('%')))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.string_symbol_box = self.string_symbol_box[:-1]

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '%')

            # Updating the string attribute(s)
            self.string_last_operand_used = '%'
            self._update_string_attributes('%')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_plus_last_pressed = True
            return
        # -----------------------------------------

    # ** SYMBOL BUTTONS SIGNALS **
    def pressed_button_clear_entry(self):
        # -- Displaying to the console --
        # print('CE has been pressed')
        # -------------------------------

        # -- Updating and clearing attributes --
        for i in self.display_box.text():
            if i == '(':
                self.left_bracket_count -= 1
            if i == ')':
                self.right_bracket_count -= 1

        self.display_box.clear()
        self.string_display_box = ''
        self.string_result = ''

        if self.symbol_box.text() == '':
            self.bool_bracket = False
            self.bool_waiting_for_operand = False
            self.bool_equal_last_pressed = False
            self._reset_symbol_flags()

        # If the button has been pressed twice call 'pressed_button_clear'
        self.clear_entry_count += 1

        if self.clear_entry_count == 2:
            self.clear_entry_count = 0
            self.pressed_button_clear()
        # --------------------------------------

    def pressed_button_clear(self):
        # -- Displaying to the console --
        # print('C has been pressed')
        # -------------------------------

        # -- Updating and clearing attributes --
        self.display_box.clear()
        self.symbol_box.clear()
        self.string_display_box = ''
        self.string_symbol_box = ''
        self.string_result = ''
        self.string_last_number_used = ''
        self.string_last_operand_used = ''
        self.left_bracket_count = 0
        self.right_bracket_count = 0
        self.bool_bracket = False
        self.bool_waiting_for_operand = False
        self.bool_equal_last_pressed = False
        self._reset_symbol_flags()
        # --------------------------------------

    def pressed_button_backspace(self):
        # -- Displaying to the console --
        # print('⌫ has been pressed')
        # -------------------------------

        # Saving a local string of the display box contents
        st = self.display_box.text()

        # If there is a bracket deleted the corresponding bracket count gets reduced
        if len(st) > 1:
            if st[-1] == ')':
                self.right_bracket_count -= 1

            if st[-1] == '(':
                self.left_bracket_count -= 1

        # special case for the **2 to allow to change the x**2 to -> x**( <mathematical expression> )
        if len(st) > 3:
            if st[-1] == '2' and st[-2] == '*' and st[-3] == '*':
                self.bool_bracket = True

        # -- Handing the input/output for the UI --
        st = st[:-1]
        self.display_box.setText(st)

        # If the 'display_box' is empty
        if not self.display_box.text():
            self.bool_waiting_for_operand = False
        # -----------------------------------------

    def pressed_button_inverse(self):
        # -- Displaying to the console --
        # print('+/- has been pressed')
        # -------------------------------

        # -- If 0 is already on the 'display_box' return --
        if self.display_box.text() == '0':
            # print("-0 Doesn't exist, i think")
            return
        # -------------------------------------------------

        # -- If the 'display_box' is empty, return --
        if not self.display_box.text():
            return
        # -------------------------------------------

        # -- Handing the input/output for the UI --
        if '-' in self.display_box.text():
            self.display_box.setText(self.display_box.text().replace('-', ''))
        else:
            self.display_box.setText('-' + self.display_box.text())
        # -----------------------------------------

    def pressed_button_dot(self):
        # -- Displaying to the console --
        # print('. has been pressed')
        # -------------------------------

        # -- If the last operand called was '=', return --
        if self.bool_equal_last_pressed:
            self.bool_equal_last_pressed = False
        # ------------------------------------------------

        # -- If the 'display_box' is empty, return --
        if not self.display_box.text():
            return
        # -------------------------------------------

        # -- If there is more than one dot , return --
        if self.display_box.text().count('.') >= 1:
            return
        # --------------------------------------------

        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + '.')
        # -----------------------------------------

    def pressed_button_left_bracket(self):
        # -- Displaying to the console --
        # print('( has been pressed')
        # -------------------------------

        # If needed the 'display_box' gets cleared
        if not self.bool_bracket:
            self.display_box.clear()

        # Increasing the left bracket count
        self.left_bracket_count = self.left_bracket_count + 1

        # Updating the flag attributes
        self.bool_bracket = True
        self.bool_equal_last_pressed = False

        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + '(')
        # -----------------------------------------

    def pressed_button_right_bracket(self):
        # -- Displaying to the console --
        # print(') has been pressed')
        # -------------------------------

        # Prevents the addition of right bracket withought a right bracket befor it
        if self.left_bracket_count < self.right_bracket_count or self.left_bracket_count == '0':
            # print('Error: Cant add ) withought enough ( before')
            return

        # Increasing the right bracket count
        self.right_bracket_count = self.right_bracket_count + 1

        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + ')')
        # -----------------------------------------

    # ** TEMPERATURE BUTTONS SIGNALS **
    def pressed_button_temperature_calculate(self):
        # -- Displaying to the console --
        # print('Temperature has been pressed')
        # -------------------------------

        x = self.button_temperature_first.currentIndex()
        y = self.button_temperature_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_temperature.clear()
        # -----------------------------------

        temp = '0'
        TEMP = 0

        if x == y:
            self.symbol_box_temperature.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            temp = str(ne.evaluate('(' + self.display_box_temperature.text() + '-272.15)'))
        elif x == 1 and y == 0:
            temp = str(ne.evaluate('(' + self.display_box_temperature.text() + '+272.15)'))
        elif x == 0 and y == 2:
            temp = str(ne.evaluate(
                '(' + '(' + '(' + '(' + self.display_box_temperature.text() + '-273.15)' + '*9)' + '/5)' + '+32)'))
        elif x == 2 and y == 0:
            temp = str(ne.evaluate(
                '(' + '(' + '(' + '(' + self.display_box_temperature.text() + '-32)' + '*5)' + '/9)' + '+273.15)'))
        elif x == 1 and y == 2:
            temp = str(ne.evaluate('(' + '(' + self.display_box_temperature.text() + '*1.8)' + '+32)'))
        elif x == 2 and y == 1:
            temp = str(ne.evaluate('(' + '(' + '(' + self.display_box_temperature.text() + '-32)' + '*5)' + '/9)'))

        # Removes unnecessary decimal points
        if x != y:
            TEMP = float(temp)
            TEMP = float("{:.2}".format(TEMP))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_temperature.setText("Το αποτέλεσμά σας είναι " + str(TEMP))
        # -----------------------------------

    # ** TIME BUTTONS SIGNALS **
    def pressed_button_time_calculate(self):
        # -- Displaying to the console --
        # print('Time has been pressed')
        # -------------------------------

        x = self.button_time_first.currentIndex()
        y = self.button_time_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_time.clear()
        # -----------------------------------

        time = '0'
        TIME = 0
        if x == y:
            self.symbol_box_time.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/60)'))
        elif x == 1 and y == 0:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*60)'))
        elif x == 0 and y == 2:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/3600)'))
        elif x == 2 and y == 0:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*3600)'))
        elif x == 0 and y == 3:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/86400)'))
        elif x == 3 and y == 0:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*86400)'))
        elif x == 0 and y == 4:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/2628002.88)'))
        elif x == 4 and y == 0:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*2628002.88)'))
        elif x == 0 and y == 5:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/31536000)'))
        elif x == 5 and y == 0:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*31536000)'))
        elif x == 1 and y == 2:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/60)'))
        elif x == 2 and y == 1:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*60)'))
        elif x == 1 and y == 3:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/1440)'))
        elif x == 3 and y == 1:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*1440)'))
        elif x == 1 and y == 4:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/0.08333333)'))
        elif x == 4 and y == 1:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*0.08333333)'))
        elif x == 1 and y == 5:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/525600)'))
        elif x == 5 and y == 1:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*525600)'))
        elif x == 2 and y == 3:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/24)'))
        elif x == 3 and y == 2:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*24)'))
        elif x == 2 and y == 4:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/730)'))
        elif x == 4 and y == 2:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*730)'))
        elif x == 2 and y == 5:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/8760)'))
        elif x == 5 and y == 2:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*8760)'))
        elif x == 3 and y == 4:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/30.4166667)'))
        elif x == 4 and y == 3:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*30.4166667)'))
        elif x == 5 and y == 3:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/365)'))
        elif x == 3 and y == 5:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*365)'))
        elif x == 4 and y == 5:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '/12)'))
        elif x == 5 and y == 4:
            time = str(ne.evaluate('(' + self.display_box_time.text() + '*12)'))

        # Removes unnecessary decimal points
        if x != y:
            TIME = float(time)
            TIME = float("{:.2}".format(TIME))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_time.setText("Το αποτέλεσμά σας είναι " + str(TIME))

        # -----------------------------------

    # ** DATE BUTTONS SIGNALS **
    def pressed_button_volume_calculate(self):
        # -- Displaying to the console --
        # print('Volume has been pressed')
        # -------------------------------

        x = self.button_volume_first.currentIndex()
        y = self.button_volume_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_volume.clear()
        # -----------------------------------
        vol = '0'
        VOL = 0

        if x == y:
            self.symbol_box_volume.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/1000000)'))
        elif x == 1 and y == 0:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*1000000)'))
        elif x == 0 and y == 2:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/1000)'))
        elif x == 2 and y == 0:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*1000)'))
        elif x == 0 and y == 3:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/35.3146667)'))
        elif x == 3 and y == 0:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*35.3146667)'))
        elif x == 0 and y == 4:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/61023.7441)'))
        elif x == 4 and y == 0:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*61023.7441)'))
        elif x == 0 and y == 5:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/1.30795062)'))
        elif x == 5 and y == 0:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*1.30795062)'))
        elif x == 1 and y == 2:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.001)'))
        elif x == 2 and y == 1:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.001)'))
        elif x == 1 and y == 3:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.00003531)'))
        elif x == 3 and y == 1:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.00003531)'))
        elif x == 1 and y == 4:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.06102374)'))
        elif x == 4 and y == 1:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.06102374)'))
        elif x == 1 and y == 5:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.00000131)'))
        elif x == 5 and y == 1:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.00000131)'))
        elif x == 2 and y == 3:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.03531467)'))
        elif x == 3 and y == 2:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.03531467)'))
        elif x == 2 and y == 4:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/61.0237441)'))
        elif x == 4 and y == 2:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*61.0237441)'))
        elif x == 2 and y == 5:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.00130795)'))
        elif x == 5 and y == 2:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.00130795)'))
        elif x == 3 and y == 4:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/1728)'))
        elif x == 4 and y == 3:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*1728)'))
        elif x == 5 and y == 3:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.03703704)'))
        elif x == 3 and y == 5:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.03703704)'))
        elif x == 4 and y == 5:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '/0.00002143)'))
        elif x == 5 and y == 4:
            vol = str(ne.evaluate('(' + self.display_box_volume.text() + '*0.00002143)'))

        # Removes unnecessary decimal points
        if x != y:
            VOL = float(vol)
            VOL = float("{:.2}".format(VOL))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_volume.setText("Το αποτέλεσμά σας είναι " + str(VOL))
        # -----------------------------------

    # ** DATA BUTTONS SIGNALS **
    def pressed_button_data_calculate(self):
        # -- Displaying to the console --
        # print('Data has been pressed')
        # -------------------------------

        x = self.button_data_first.currentIndex()
        y = self.button_data_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_data.clear()
        # -----------------------------------
        data = '0'
        DATA = 0

        if x == y:
            self.symbol_box_data.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.125)'))
        elif x == 1 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.125)'))
        elif x == 0 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.000125)'))
        elif x == 2 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.000125)'))
        elif x == 0 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.000000125)'))
        elif x == 3 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.000000125)'))
        elif x == 0 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.000000000125)'))
        elif x == 4 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.000000000125)'))
        elif x == 0 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.000000000000125)'))
        elif x == 5 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.000000000000125)'))
        elif x == 0 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.000000000000125)'))
        elif x == 6 and y == 0:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.000000000000125)'))
        elif x == 1 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.001)'))
        elif x == 2 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.001)'))
        elif x == 1 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000010)'))
        elif x == 3 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000010)'))
        elif x == 1 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000010)'))
        elif x == 4 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000010)'))
        elif x == 1 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000000010)'))
        elif x == 5 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000000010)'))
        elif x == 1 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000000000010)'))
        elif x == 6 and y == 1:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000000000010)'))
        elif x == 2 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.001)'))
        elif x == 3 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.001)'))
        elif x == 2 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000010)'))
        elif x == 4 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000010)'))
        elif x == 2 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000010)'))
        elif x == 5 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000010)'))
        elif x == 2 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000000010)'))
        elif x == 6 and y == 2:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000000010)'))
        elif x == 3 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.001)'))
        elif x == 4 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.001)'))
        elif x == 3 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000010)'))
        elif x == 5 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000010)'))
        elif x == 3 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000000010)'))
        elif x == 6 and y == 3:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000000010)'))
        elif x == 4 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.001)'))
        elif x == 5 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.001)'))
        elif x == 4 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.0000010)'))
        elif x == 6 and y == 4:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.0000010)'))
        elif x == 5 and y == 6:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '/0.001)'))
        elif x == 6 and y == 5:
            data = str(ne.evaluate('(' + self.display_box_data.text() + '*0.001)'))

        # Removes unnecessary decimal points
        if x != y:
            DATA = float(data)
            DATA = float("{:.2}".format(DATA))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_data.setText("Το αποτέλεσμά σας είναι " + str(DATA))
        # -----------------------------------

    # ** DISCOUNT BUTTONS SIGNALS **
    def pressed_button_discount_calculate(self):
        # -- Displaying to the console --
        # print('Discount has been pressed')
        # -------------------------------

        # Clears the box that displays the results
        self.symbol_box_discount.clear()
        # -----------------------------------

        discount = '0'
        DISCOUNT = 0

        discount = str(ne.evaluate(
            '(' + self.display_box_discount.text() + '-' + '(' + self.display_box_discount.text() + '*' + '(' + self.display_box_discount1.text() + '/100' + ')' + ')' + ')'))

        # Removes unnecessary decimal points
        DISCOUNT = float(discount)
        DISCOUNT = float("{:.2}".format(DISCOUNT))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        self.symbol_box_discount.setText("Το αποτέλεσμά σας είναι " + str(DISCOUNT))
        # -----------------------------------

    # ** AGE BUTTONS SIGNALS **
    def pressed_button_age_calculate(self):
        # -- Displaying to the console --
        # print('Age has been pressed')
        # -------------------------------
        # Getting the current time
        today = datetime.today()

        # Getting the date in the display
        x = self.symbol_box_age.text()
        st = x.split("/")
        if len(st) != 3:
            return
        birth = datetime.strptime(x, "%d/%m/%Y")
        age = today - birth
        days = age.days
        full_age = "{0} years {1} months {2} days old".format(str(math.floor(days / 365)),
                                                              str(math.floor(days % 365 / 30)),
                                                              str(math.floor(days % 365 % 31)))
        self.symbol_box_age.setText(full_age)

    def pressed_button_age_clear(self):
        # Clears the box that displays the results
        self.symbol_box_age.clear()
        # -----------------------------------

    # ** MASS BUTTONS SIGNALS **
    def pressed_button_mass_calculate(self):
        # -- Displaying to the console --
        # print('Mass has been pressed')
        # -------------------------------

        x = self.button_mass_first.currentIndex()
        y = self.button_mass_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_mass.clear()
        # -----------------------------------

        mass = '0'
        MASS = 0

        if x == y:
            self.symbol_box_mass.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/2.20462262)'))
        elif x == 1 and y == 0:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*2.20462262)'))
        elif x == 0 and y == 2:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/35.2739619)'))
        elif x == 2 and y == 0:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*35.2739619)'))
        elif x == 0 and y == 3:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/5000)'))
        elif x == 3 and y == 0:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*5000)'))
        elif x == 0 and y == 4:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/1000)'))
        elif x == 4 and y == 0:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*1000)'))
        elif x == 1 and y == 2:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/16)'))
        elif x == 2 and y == 1:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*16)'))
        elif x == 1 and y == 3:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/2267.96185)'))
        elif x == 3 and y == 1:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*2267.96185)'))
        elif x == 1 and y == 4:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/453.59237)'))
        elif x == 4 and y == 1:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*453.59237)'))
        elif x == 2 and y == 3:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/141.747616)'))
        elif x == 3 and y == 2:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*141.747616)'))
        elif x == 2 and y == 4:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/28.3495231)'))
        elif x == 4 and y == 2:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*28.3495231)'))
        elif x == 3 and y == 4:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '/0.2)'))
        elif x == 4 and y == 3:
            mass = str(ne.evaluate('(' + self.display_box_mass.text() + '*0.2)'))

        # Removes unnecessary decimal points
        if x != y:
            MASS = float(mass)
            MASS = float("{:.2}".format(MASS))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_mass.setText("Το αποτέλεσμά σας είναι " + str(MASS))
        # -----------------------------------

    # ** SPEED BUTTONS SIGNALS **
    def pressed_button_speed_calculate(self):
        # -- Displaying to the console --
        # print('Speed has been pressed')
        # -------------------------------

        x = self.button_speed_first.currentIndex()
        y = self.button_speed_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_speed.clear()
        # -----------------------------------

        speed = '0'
        SPEED = 0

        if x == y:
            self.symbol_box_speed.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.62137119)'))
        elif x == 1 and y == 0:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.62137119)'))
        elif x == 0 and y == 2:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/1000)'))
        elif x == 2 and y == 0:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*1000)'))
        elif x == 0 and y == 3:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/3280.83989501)'))
        elif x == 3 and y == 0:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*3280.83989501)'))
        elif x == 0 and y == 4:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.00080985)'))
        elif x == 4 and y == 0:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.00080985)'))
        elif x == 0 and y == 5:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.5399568)'))
        elif x == 5 and y == 0:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.5399568)'))
        elif x == 1 and y == 2:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/1609.344)'))
        elif x == 2 and y == 1:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*1609.344)'))
        elif x == 1 and y == 3:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/5280)'))
        elif x == 3 and y == 1:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*5280)'))
        elif x == 1 and y == 4:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.00130332)'))
        elif x == 4 and y == 1:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.00130332)'))
        elif x == 1 and y == 5:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.86897624)'))
        elif x == 5 and y == 1:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.86897624)'))
        elif x == 2 and y == 3:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/3.2808399)'))
        elif x == 3 and y == 2:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*3.2808399)'))
        elif x == 2 and y == 4:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.0030184123)'))
        elif x == 4 and y == 2:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.0030184123)'))
        elif x == 2 and y == 5:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.0005399568034557236)'))
        elif x == 5 and y == 2:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.0005399568034557236)'))
        elif x == 3 and y == 4:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.00092001207)'))
        elif x == 4 and y == 3:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.00092001207)'))
        elif x == 5 and y == 3:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/0.00016457883)'))
        elif x == 3 and y == 5:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*0.00016457883)'))
        elif x == 4 and y == 5:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '/666.738661)'))
        elif x == 5 and y == 4:
            speed = str(ne.evaluate('(' + self.display_box_speed.text() + '*666.738661)'))

        # Removes unnecessary decimal points
        if x != y:
            SPEED = float(speed)
            SPEED = float("{:.2}".format(SPEED))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_speed.setText("Το αποτέλεσμά σας είναι " + str(SPEED))

        # -----------------------------------

    # ** LENGTH BUTTONS SIGNALS **
    def pressed_button_length_calculate(self):
        # -- Displaying to the console --
        # print('Length has been pressed')
        # -------------------------------

        x = self.button_length_first.currentIndex()
        y = self.button_length_second.currentIndex()

        # Clears the box that displays the results
        self.symbol_box_length.clear()
        # -----------------------------------

        length = '0'
        LENGTH = 0

        if x == y:
            self.symbol_box_length.setText("Η τιμή που εισαγάγατε είναι ίδιου τύπου με του αποτελέσματός σας.")
        elif x == 0 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/3.2808399)'))
        elif x == 1 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*3.2808399)'))
        elif x == 0 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.001)'))
        elif x == 2 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.001)'))
        elif x == 0 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00062137)'))
        elif x == 3 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00062137)'))
        elif x == 0 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/39.3700787)'))
        elif x == 4 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*39.3700787)'))
        elif x == 0 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/1.0936133)'))
        elif x == 5 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*1.0936133)'))
        elif x == 0 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00053996)'))
        elif x == 6 and y == 0:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00053996)'))
        elif x == 1 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.0003048)'))
        elif x == 2 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.0003048)'))
        elif x == 1 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00018939)'))
        elif x == 3 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00018939)'))
        elif x == 1 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/12)'))
        elif x == 4 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*12)'))
        elif x == 1 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.33333333)'))
        elif x == 5 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.33333333)'))
        elif x == 1 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00016458)'))
        elif x == 6 and y == 1:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00016458)'))
        elif x == 2 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.62137119)'))
        elif x == 3 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.62137119)'))
        elif x == 2 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/39370.0787)'))
        elif x == 4 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*39370.0787)'))
        elif x == 2 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/1093.6133)'))
        elif x == 5 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*1093.6133)'))
        elif x == 2 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.5399568)'))
        elif x == 6 and y == 2:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.5399568)'))
        elif x == 3 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/63360)'))
        elif x == 4 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*63360)'))
        elif x == 3 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/1760)'))
        elif x == 5 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*1760)'))
        elif x == 3 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.86897624)'))
        elif x == 6 and y == 3:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.86897624)'))
        elif x == 4 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.02777778)'))
        elif x == 5 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.02777778)'))
        elif x == 4 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00001371)'))
        elif x == 6 and y == 4:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00001371)'))
        elif x == 5 and y == 6:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '/0.00049374)'))
        elif x == 6 and y == 5:
            length = str(ne.evaluate('(' + self.display_box_length.text() + '*0.00049374)'))

        # Removes unnecessary decimal points
        if x != y:
            LENGTH = float(length)
            LENGTH = float("{:.2}".format(LENGTH))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if x != y:
            self.symbol_box_length.setText("Το αποτέλεσμά σας είναι " + str(LENGTH))
        # -----------------------------------

    # ** BMI BUTTONS SIGNALS **
    def pressed_button_bmi_calculate(self):
        # -- Displaying to the console --
        # print('BMI has been pressed')
        # -------------------------------

        # Clears the box that displays the results
        self.symbol_box_bmi.clear()
        # -----------------------------------

        # Selects the right algorithms based on which button u have chosen
        if self.button_bmi_first.currentIndex() == 0:
            bmi = str(ne.evaluate('(' + self.display_box_bmi.text() + ')/('
                                  + self.display_box_bmi1.text() + '/100) ** 2'))
        else:
            bmi = str(ne.evaluate('(' + self.display_box_bmi.text() + '/'
                                  + self.display_box_bmi1.text() + '/'
                                  + self.display_box_bmi1.text() + ')*703'))
        # -----------------------------------

        # Removes unnecessary decimal points
        BMI = float(bmi)

        BMI = float("{:.2}".format(BMI))
        # -----------------------------------

        # -- Handing the input/output for the UI --
        if BMI <= 18.4:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε λιποβαρής.")
        elif BMI <= 24.9:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε υγειής.")
        elif BMI <= 29.9:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε υπέρβαροι.")
        elif BMI <= 34.9:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε σοβαρά υπέρβαροι.")
        elif BMI <= 39.9:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε παχύσαρκοι.")
        elif BMI > 39.9:
            self.symbol_box_bmi.setText("Ο ΔΜΣ σας ειναι " + str(BMI) + ". Είστε σοβαρά παχύσαρκοι.")
        # -----------------------------------

    # ** MENU & ACTION SIGNALS **
    def pressed_button_background_color(self):
        # -- Displaying to the console --
        # print('Background color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title="Επιλογή Χρώματος Φόντου")
        self.palette.setColor(QPalette.Window, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_text_color(self):
        # -- Displaying to the console --
        # print('Text color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Επιλογή Χρώματος Κειμένου')
        self.palette.setColor(QPalette.ButtonText, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_color(self):
        # -- Displaying to the console --
        # print('Button color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Επιλογή Χρώματος Κουμπιών')
        self.palette.setColor(QPalette.Button, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_display_color(self):
        # -- Displaying to the console --
        # print('Display color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Επιλογή Χρώματος Οθόνης')
        self.palette.setColor(QPalette.Base, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_display_text(self):
        # -- Displaying to the console --
        # print("Display text's color button has been pressed")
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title="Επιλογή Χρώματος Κειμένου Οθόνης")
        self.palette.setColor(QPalette.Text, color)
        color = QColorDialog.getColor(title="Επιλογή Χρώματος Επισημασμένου Κειμένου Οθόνης")
        self.palette.setColor(QPalette.HighlightedText, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def clicked_help_about(self):
        # -- Displaying to the console --
        # print('About has been pressed')

        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        self._QMenuBar_global_signals()
        # --------------

        # ----- QFont ------
        font_Qlabel = QFont()
        font_Qlabel.setPointSize(font_Qlabel.pointSize() + 2)
        # ------------------

        # Making the QLabel and QScrollArea
        self.info_label = QLabel('''    -- HOW TO USE --
    Είναι πρακτικά μία κοινή αριθμομηχανή
    στα ελληνικά όπου σας επιτρέπεται η
    εκτέλεση απλών πράξεων.

    Δίνεται η δυνατότητα να γράψετε
    από πληκτρολόγιο ή από το UI που 
    έχουμε δημιουργήσει. Προσοχή όμως η
    μίξη των δυο μπορεί να δημιουργήσει
    προβλήματα! 

    Η εκτέλεση των πράξεων γίνεται με
    τον υπολογισμό Strings, χωρίς την
    αποκλειστική χρήση του eval το οποίο
    θεωρείται επικίνδυνο.

    Αλγόριθμοι και σύμβολα
    X² = x**2 
    X Mod y = x%y 
    |x| = abs(x) 
    √x = sqrt(x) 
    Log(x) = log10(x) 
    Ln(x) = log(x) 
    Συν(x) = sin(x) 
    Ημ(x) = cos(x) 
    Εφ(x) = tan(x) 

    Το παραγοντικό δεν υποστηρίζεται
    δυστυχώς.

    Επιπλέων παρέχεται η δυνατότητα να 
    κάνετε μετατροπές μονάδων καθώς και
    υπολογισμό του δείκτη μάζας σωματός
    σας (ΔΜΣ ή BMI).

    Τέλος, μπορείτε να αλλάξετε ορισμένα
    χρώματα αντικειμένων του UI, αλλά και
    να επιλέξετε μεταξύ δύο διαφορετικών
    προκατασκευασμένων θεμάτων.

    - - Creators - -
    Vasilis
    Thanosks
    Xarison
    Panagos
    - - - - - - - - - -
''')
        self.info_label.setFont(font_Qlabel)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.about_scroll_area = QScrollArea()
        self.about_scroll_area.setWidget(self.info_label)
        # -------------------------------------

        # ------ QGridLayout() --------
        self.layout_grid_about = QGridLayout()
        self.layout_grid_about.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_about.setSpacing(1.8)

        # Setting the widget objects in the QGridLayout
        self.layout_grid_about.addWidget(self.menu_bar, 0, 0, 1, 4)
        self.layout_grid_about.addWidget(self.about_scroll_area, 1, 0, 1, 4)
        # -----------------------------------

        # Making the widget, setting its layout and setting it as central widget
        self.widget_calculator_about = QWidget()
        self.widget_calculator_about.setLayout(self.layout_grid_about)
        self.setCentralWidget(self.widget_calculator_about)
        # -----------------------------------------

    # ** MENU & ACTION SIGNALS **
    def pressed_STANDARD(self):
        # -- Displaying to the console --
        # print("Standard button has been pressed")
        # -------------------------------
        self._QWidget_calculator_standard()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_SCIENTIFIC(self):
        # -- Displaying to the console --
        # print('scientific has been pressed')
        # -------------------------------
        self._QWidget_calculator_scientific()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_TEMPERATURE(self):
        # -- Displaying to the console --
        # print("Temperature button has been pressed")
        # -------------------------------
        self._QWidget_calculator_temperature()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_TIME(self):
        # -- Displaying to the console --
        # print("Time button has been pressed")
        # -------------------------------
        self._QWidget_calculator_time()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_VOLUME(self):
        # -- Displaying to the console --
        # print("Date button has been pressed")
        # -------------------------------
        self._QWidget_calculator_volume()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_DATA(self):
        # -- Displaying to the console --
        # print("Data button has been pressed")
        # -------------------------------
        self._QWidget_calculator_data()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_DISCOUNT(self):
        # -- Displaying to the console --
        # print("Discount button has been pressed")
        # -------------------------------
        self._QWidget_calculator_discount()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_AGE(self):
        # -- Displaying to the console --
        # print("Age button has been pressed")
        # -------------------------------
        self._QWidget_calculator_age()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_MASS(self):
        # -- Displaying to the console --
        # print("Mass button has been pressed")
        # -------------------------------
        self._QWidget_calculator_mass()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_SPEED(self):
        # -- Displaying to the console --
        # print("Speed button has been pressed")
        # -------------------------------
        self._QWidget_calculator_speed()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_LENGTH(self):
        # -- Displaying to the console --
        # print("Length button has been pressed")
        # -------------------------------
        self._QWidget_calculator_length()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_BMI(self):
        # -- Displaying to the console --
        # print("BMI button has been pressed")
        # -------------------------------
        self._QWidget_calculator_bmi()
        self.bool_temp_modes = True
        # ------------------------------------
    # -------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())
