# This still needs work so im not putting it in the same file as the old calculator
# - Thanosks

import sys
import numexpr as ne
import numpy as np
import math
from PySide6.QtGui import (QAction, QFont, QIcon, QPalette, QColor)
from PySide6.QtCore import (Qt, Slot, QRect)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton,
                               QSizePolicy, QMenuBar, QColorDialog, QComboBox)


class Calculator(QMainWindow):
    # ** CLASS PROPERTIES **
    def _QMainWindow_properties(self):
        # -- Assigning our QWidget's properties --
        QWidget.setWindowTitle(self, "Calculator")
        QWidget.setWindowIcon(self, QIcon('pics/calc1.png'))
        QWidget.setGeometry(self, 450, 220, 330, 330)
        # --------------------------------------

    # ** DECLARATION FUNCTIONS **
    def _calculator_modes_declarations(self):
        # ** DECLARATION & ALTERING OF THE CALCULATOR ATTRIBUTES **
        # It contains all the common attributes across calculator modes

        # -- Declaration of count for the correct use of brackets in scientific mode --
        self.left_bracket_count = 0
        self.right_bracket_count = 0

        # -- Boolean attributes --
        self.bool_dont_del = False  # To prevent the deletion of display_box's contents in some occasions
        self.bool_waiting_for_operand = False  # Set to False so it doesn't display a symbol that's pressed on its first run
        self.bool_equal_last_pressed = False  # To check whether the last symbol pressed was a '=' sign
        self.bool_plus_last_pressed = False  # To check whether the last symbol pressed was a '+' sign
        self.bool_minus_last_pressed = False  # To check whether the last symbol pressed was a '-' sign
        self.bool_times_last_pressed = False  # To check whether the last symbol pressed was a '*' sign
        self.bool_division_last_pressed = False  # To check whether the last symbol pressed was a '/' sign
        self.bool_modular_last_pressed = False  # To check whether the last symbol pressed was a 'Mod' sign
        # ------------------------
        # -- String attributes --
        self.string_display_box = ''  # Contains the contents of the 'display_box'
        self.string_symbol_box = ''  # Contains the contents of the 'symbol_box'
        self.string_display_box_SCI = ''  # Contains the contents of the 'display_box_SCI'
        self.string_symbol_box_SCI = ''  # Contains the contents of the 'symbol_box_SCI'
        self.string_display_box_TIME = ''  # Contains the contents of the 'display_box_TIME'
        self.string_symbol_box_TIME = ''  # Contains the contents of the 'symbol_box_TIME'
        self.string_display_box_DATA = ''  # Contains the contents of the 'display_box_DATA'
        self.string_symbol_box_DATA = ''  # Contains the contents of the 'symbol_box_DATA'
        self.string_display_box_TEMP = ''  # Contains the contents of the 'display_box_TEMP'
        self.string_symbol_box_TEMP = ''  # Contains the contents of the 'symbol_box_TEMP'
        self.string_display_box_LEN = ''  # Contains the contents of the 'display_box_LEN'
        self.string_symbol_box_LEN = ''  # Contains the contents of the 'symbol_box_LEN'
        self.string_display_box_MASS = ''  # Contains the contents of the 'display_box_MASS'
        self.string_symbol_box_MASS = ''  # Contains the contents of the 'symbol_box_MASS'
        self.string_display_box_SPEED = ''  # Contains the contents of the 'display_box_SPEED'
        self.string_symbol_box_SPEED = ''  # Contains the contents of the 'symbol_box_SPEED'
        self.string_display_box_AGE = ''  # Contains the contents of the 'display_box_AGE'
        self.string_display_box_AGE_2 = ''  # Contains the contents of the 'display_box_AGE_2'
        self.string_symbol_box_AGE = ''  # Contains the contents of the 'symbol_box_AGE'
        self.string_display_box_DISC = ''  # Contains the contents of the 'display_box_DISC'
        self.string_display_box_DISC_2 = ''  # Contains the contents of the 'display_box_DISC_2'
        self.string_symbol_box_DISC = ''  # Contains the contents of the 'symbol_box_DISC'
        self.string_display_box_BMI = ''  # Contains the contents of the 'display_box_BMI'
        self.string_display_box_BMI_2 = ''  # Contains the contents of the 'display_box_BMI_2'
        self.string_symbol_box_BMI = ''  # Contains the contents of the 'symbol_box_BMI'
        self.string_display_box_DATE = ''  # Contains the contents of the 'display_box_DATE'
        self.string_display_box_DATE_2 = ''  # Contains the contents of the 'display_box_DATE_2'
        self.string_symbol_box_DATE = ''  # Contains the contents of the 'symbol_box_DATE'
        self.string_result = ''  # Contains the contents of the complete string
        self.string_last_operand_used = ''  # Contains the contents of the last operand used (excluding = operand)
        self.string_last_number_used = ''  # Contains the contents of the last number used
        self.string_calculated_invoked = ''  # Contains the contents of the function '_calculated_invoked'
        # -----------------------
        # -- QLineEdit attributes --
        self.display_box = QLineEdit('')
        self.symbol_box = QLineEdit('')
        self.symbol_box_SCI = QLineEdit('')
        self.display_box_SCI = QLineEdit('')
        self.display_box_TIME = QLineEdit('Enter your value here.')
        self.symbol_box_TIME = QLineEdit('')
        self.display_box_DATA = QLineEdit('Enter your value here.')
        self.symbol_box_DATA = QLineEdit('')
        self.display_box_TEMP = QLineEdit('Enter your value here.')
        self.symbol_box_TEMP = QLineEdit('')
        self.display_box_LEN = QLineEdit('Enter your value here.')
        self.symbol_box_LEN = QLineEdit('')
        self.display_box_MASS = QLineEdit('Enter your value here.')
        self.symbol_box_MASS = QLineEdit('')
        self.display_box_SPEED = QLineEdit('Enter your value here.')
        self.symbol_box_SPEED = QLineEdit('')
        self.display_box_AGE = QLineEdit('Enter your birth year.')
        self.display_box_AGE_2 = QLineEdit('Enter the current year.')
        self.symbol_box_AGE = QLineEdit('')
        self.display_box_DISC = QLineEdit('Enter the original price.')
        self.display_box_DISC_2 = QLineEdit('Enter the discount.')
        self.symbol_box_DISC = QLineEdit('')
        self.display_box_BMI = QLineEdit('Enter your weight here.')
        self.display_box_BMI_2 = QLineEdit('Enter your height here.')
        self.symbol_box_BMI = QLineEdit('')
        self.display_box_DATE = QLineEdit('Enter the first value here.')
        self.display_box_DATE_2 = QLineEdit('Enter the second value here.')
        self.symbol_box_DATE = QLineEdit('')
        # --------------------------
        # -- QPushButton attributes --
        #       * Algebraic buttons
        self.button_exponent = QPushButton('x²')
        self.button_raise = QPushButton('xⁿ')
        self.button_absolute = QPushButton('|x|')
        self.button_sqrt = QPushButton('√')
        self.button_log = QPushButton('log')
        self.button_ln = QPushButton('ln')
        self.button_pi = QPushButton('π')
        self.button_factorial = QPushButton('n!')

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

        #       * Discount buttons
        self.button_CalculateDiscount = QPushButton("Calculate Discount")

        #       * Temperature buttons
        self.button_FirstTemp = QComboBox()
        self.button_FirstTemp.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstTemp.addItem("Kelvin")
        self.button_FirstTemp.addItem("Celsius")
        self.button_FirstTemp.addItem("Fahrenheit")
        self.button_FirstTemp.setCurrentIndex(0)

        self.button_SecondTemp = QComboBox()
        self.button_SecondTemp.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondTemp.addItem("Kelvin")
        self.button_SecondTemp.addItem("Celsius")
        self.button_SecondTemp.addItem("Fahrenheit")
        self.button_SecondTemp.setCurrentIndex(0)

        self.button_CalculateTemp = QPushButton("Calculate Temperature")

        #       * Data buttons
        self.button_FirstData = QComboBox()
        self.button_FirstData.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstData.addItem("Bits")
        self.button_FirstData.addItem("Bytes")
        self.button_FirstData.addItem("KiloBytes")
        self.button_FirstData.addItem("MegaBytes")
        self.button_FirstData.addItem("GigaBytes")
        self.button_FirstData.addItem("TeraBytes")
        self.button_FirstData.addItem("PetaBytes")
        self.button_FirstData.setCurrentIndex(0)

        self.button_SecondData = QComboBox()
        self.button_SecondData.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondData.addItem("Bits")
        self.button_SecondData.addItem("Bytes")
        self.button_SecondData.addItem("KiloBytes")
        self.button_SecondData.addItem("MegaBytes")
        self.button_SecondData.addItem("GigaBytes")
        self.button_SecondData.addItem("TeraBytes")
        self.button_SecondData.addItem("PetaBytes")
        self.button_SecondData.setCurrentIndex(0)

        self.button_CalculateData = QPushButton("Calculate Data")

        #       * Age buttons
        self.button_CalculateAge = QPushButton("Calculate Age")

        #       * Time buttons
        self.button_FirstTime = QComboBox()
        self.button_FirstTime.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstTime.addItem("Seconds")
        self.button_FirstTime.addItem("Minutes")
        self.button_FirstTime.addItem("Hours")
        self.button_FirstTime.addItem("Days")
        self.button_FirstTime.addItem("Months")
        self.button_FirstTime.addItem("Years")
        self.button_FirstTime.setCurrentIndex(0)

        self.button_SecondTime = QComboBox()
        self.button_SecondTime.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondTime.addItem("Seconds")
        self.button_SecondTime.addItem("Minutes")
        self.button_SecondTime.addItem("Hours")
        self.button_SecondTime.addItem("Days")
        self.button_SecondTime.addItem("Months")
        self.button_SecondTime.addItem("Years")
        self.button_SecondTime.setCurrentIndex(0)

        self.button_CalculateTime = QPushButton("Calculate Time")

        #       * BMI buttons
        self.button_FirstBMI = QComboBox()
        self.button_FirstBMI.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstBMI.addItem("KGs/Meters")
        self.button_FirstBMI.addItem("Pounds/Inches")
        self.button_FirstBMI.setCurrentIndex(0)

        self.button_CalculateBMI = QPushButton("Calculate BMI")

        #       * Date buttons
        self.button_CalculateDATE = QPushButton("Calculate Date")

        #       * Length buttons
        self.button_FirstLength = QComboBox()
        self.button_FirstLength.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstLength.addItem("Meters")
        self.button_FirstLength.addItem("Feet")
        self.button_FirstLength.addItem("Kilometers")
        self.button_FirstLength.addItem("Miles")
        self.button_FirstLength.addItem("Inches")
        self.button_FirstLength.addItem("Yards")
        self.button_FirstLength.addItem("Nautical Miles")
        self.button_FirstLength.setCurrentIndex(0)

        self.button_SecondLength = QComboBox()
        self.button_SecondLength.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondLength.addItem("Meters")
        self.button_SecondLength.addItem("Feet")
        self.button_SecondLength.addItem("Kilometers")
        self.button_SecondLength.addItem("Miles")
        self.button_SecondLength.addItem("Inches")
        self.button_SecondLength.addItem("Yards")
        self.button_SecondLength.addItem("Nautical Miles")
        self.button_SecondLength.setCurrentIndex(0)

        self.button_CalculateLength = QPushButton("Calculate Length")

        #       * Mass buttons
        self.button_FirstMass = QComboBox()
        self.button_FirstMass.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstMass.addItem("Kilograms")
        self.button_FirstMass.addItem("Pounds")
        self.button_FirstMass.addItem("Ounces")
        self.button_FirstMass.addItem("Carats")
        self.button_FirstMass.addItem("Grams")
        self.button_FirstMass.setCurrentIndex(0)

        self.button_SecondMass = QComboBox()
        self.button_SecondMass.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondMass.addItem("Kilograms")
        self.button_SecondMass.addItem("Pounds")
        self.button_SecondMass.addItem("Ounces")
        self.button_SecondMass.addItem("Carats")
        self.button_SecondMass.addItem("Grams")
        self.button_SecondMass.setCurrentIndex(0)

        self.button_CalculateMass = QPushButton("Calculate Mass")

        #       * Speed buttons
        self.button_FirstSpeed = QComboBox()
        self.button_FirstSpeed.setGeometry(QRect(10, 10, 10, 10))
        self.button_FirstSpeed.addItem("Kilometers/h")
        self.button_FirstSpeed.addItem("Miles/h")
        self.button_FirstSpeed.addItem("Meters/s")
        self.button_FirstSpeed.addItem("Feet/s")
        self.button_FirstSpeed.addItem("Machs")
        self.button_FirstSpeed.addItem("Knots")
        self.button_FirstSpeed.setCurrentIndex(0)

        self.button_SecondSpeed = QComboBox()
        self.button_SecondSpeed.setGeometry(QRect(10, 10, 10, 10))
        self.button_SecondSpeed.addItem("Kilometers/h")
        self.button_SecondSpeed.addItem("Miles/h")
        self.button_SecondSpeed.addItem("Meters/s")
        self.button_SecondSpeed.addItem("Feet/s")
        self.button_SecondSpeed.addItem("Machs")
        self.button_SecondSpeed.addItem("Knots")
        self.button_SecondSpeed.setCurrentIndex(0)

        self.button_CalculateSpeed = QPushButton("Calculate Speed")
        # ----------------------------

    #   FOR THE STANDARD CALCULATOR MODE
    def _QLineEdit_standard_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------
        self.Dark_Theme()
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box.setReadOnly(False)
        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(1000)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(250)
        self.symbol_box.setFont(font_symbol_box)
        # -------------------------------------------------------------

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
        self.layout_grid_standard.addWidget(self.button_times, 4, 4)
        #       Regards the fifth row of the grid
        self.layout_grid_standard.addWidget(self.button_minus, 5, 4)
        #       Regards the sixth row of the grid
        self.layout_grid_standard.addWidget(self.button_plus, 6, 4)
        #       Regards the seventh row of the grid
        self.layout_grid_standard.addWidget(self.button_inverse, 7, 1)
        self.layout_grid_standard.addWidget(self.button_dot, 7, 3)
        self.layout_grid_standard.addWidget(self.button_equal, 7, 4)
        # ------------------------------

    def _QPushButton_standard_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()

        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------

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

    def _Make_Num_Buttons(self, mode='st'):
        names = ('7', '8', '9', '4', '5', '6', '1', '2', '3', '0')

        k = 0
        if mode == 'sc':
            k = 1
        j = 4 + (k * 2)
        i = 1 + k

        for n, name in enumerate(names):
            self.button = QPushButton(name, self)

            self.button.clicked.connect(self.NumButton_call(name))

            self.button.setFont(self.font_button)

            self.button.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

            if name != '0':
                if mode == 'sc':
                    self.layout_grid_scientific.addWidget(self.button, j, i)
                else:
                    self.layout_grid_standard.addWidget(self.button, j, i)

                i = i + 1
                if i == 4 + k:
                    j = j + 1
                    i = 1 + k
            else:
                if mode == 'sc':
                    self.layout_grid_scientific.addWidget(self.button, 9, 3)
                else:
                    self.layout_grid_standard.addWidget(self.button, 7, 2)

    #   FOR THE TEMPERATURE CALCULATOR MODE
    def _QLineEdit_temperature_properties(self):

        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_TEMP = QFont()
        font_symbol_box_TEMP = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_TEMP' attribute
        font_display_box_TEMP.setPointSize(font_display_box_TEMP.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_TEMP' attribute
        font_symbol_box_TEMP.setPointSize(font_symbol_box_TEMP.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        self.display_box_TEMP.setReadOnly(False)
        self.display_box_TEMP.setAlignment(Qt.AlignRight)
        self.display_box_TEMP.setMaxLength(25)
        self.display_box_TEMP.setFont(font_display_box_TEMP)

        self.symbol_box_TEMP.setFont(font_symbol_box_TEMP)
        self.symbol_box_TEMP.setMaxLength(25)
        self.symbol_box_TEMP.setAlignment(Qt.AlignRight)
        self.symbol_box_TEMP.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_temperature_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_temperature.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_temperature.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_temperature_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Temperature buttons
        self.button_FirstTemp.setFont(self.font_button)
        self.button_SecondTemp.setFont(self.font_button)
        self.button_CalculateTemp.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Temperature buttons
        self.button_FirstTemp.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondTemp.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_CalculateTemp.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_temperature(self):
        # -- Our 'Temperature' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_temperature.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_temperature.addWidget(self.display_box_TEMP, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_temperature.addWidget(self.symbol_box_TEMP, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_temperature.addWidget(self.button_FirstTemp, 4, 1)
        self.layout_grid_temperature.addWidget(self.button_SecondTemp, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_temperature.addWidget(self.button_CalculateTemp, 6, 2)

    #   FOR THE DATE CALCULATOR MODE
    def _QLineEdit_date_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_DATE = QFont()
        font_display_box_DATE_2 = QFont()
        font_symbol_box_DATE = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_DATE' attribute
        font_display_box_DATE.setPointSize(font_display_box_DATE.pointSize() + 10)
        # For the QLineEdit 'font_display_box_DATE_2' attribute
        font_display_box_DATE_2.setPointSize(font_display_box_DATE_2.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_DATA' attribute
        font_symbol_box_DATE.setPointSize(font_symbol_box_DATE.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Date

        self.display_box_DATE.setReadOnly(False)
        self.display_box_DATE.setAlignment(Qt.AlignRight)
        self.display_box_DATE.setMaxLength(25)
        self.display_box_DATE.setFont(font_display_box_DATE)

        self.display_box_DATE_2.setReadOnly(False)
        self.display_box_DATE_2.setAlignment(Qt.AlignRight)
        self.display_box_DATE_2.setMaxLength(25)
        self.display_box_DATE_2.setFont(font_display_box_DATE_2)

        self.symbol_box_DATE.setFont(font_symbol_box_DATE)
        self.symbol_box_DATE.setMaxLength(25)
        self.symbol_box_DATE.setAlignment(Qt.AlignRight)
        self.symbol_box_DATE.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_date_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_date.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_date.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_date_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Date buttons
        self.button_CalculateDATE.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Date buttons
        self.button_CalculateDATE.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_date(self):
        # -- Our 'Date' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_date.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_date.addWidget(self.button_CalculateDATE, 5, 1)

        #       Regards the fourth row of the grid
        self.layout_grid_date.addWidget(self.display_box_DATE, 3, 1, 1, 4)

        #       Regards the fifth row of the grid
        self.layout_grid_date.addWidget(self.display_box_DATE_2, 4, 1, 1, 4)

        #       Regards the sixth row of the grid
        self.layout_grid_date.addWidget(self.symbol_box_DATE, 6, 1, 1, 4)

    #   FOR THE AGE CALCULATOR MODE
    def _QLineEdit_age_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_AGE = QFont()
        font_display_box_AGE_2 = QFont()
        font_symbol_box_AGE = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_AGE' attribute
        font_display_box_AGE.setPointSize(font_display_box_AGE.pointSize() + 10)
        # For the QLineEdit 'font_display_box_AGE_2' attribute
        font_display_box_AGE_2.setPointSize(font_display_box_AGE_2.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_AGE' attribute
        font_symbol_box_AGE.setPointSize(font_symbol_box_AGE.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Age

        self.display_box_AGE.setReadOnly(False)
        self.display_box_AGE.setAlignment(Qt.AlignRight)
        self.display_box_AGE.setMaxLength(25)
        self.display_box_AGE.setFont(font_display_box_AGE)

        self.display_box_AGE_2.setReadOnly(False)
        self.display_box_AGE_2.setAlignment(Qt.AlignRight)
        self.display_box_AGE_2.setMaxLength(25)
        self.display_box_AGE_2.setFont(font_display_box_AGE_2)

        self.symbol_box_AGE.setFont(font_symbol_box_AGE)
        self.symbol_box_AGE.setMaxLength(25)
        self.symbol_box_AGE.setAlignment(Qt.AlignRight)
        self.symbol_box_AGE.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_age_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_age.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_age.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_age_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Age buttons
        self.button_CalculateAge.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Age buttons
        self.button_CalculateAge.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_age(self):
        # -- Our 'Age' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_age.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_age.addWidget(self.button_CalculateAge, 5, 1)

        #       Regards the fourth row of the grid
        self.layout_grid_age.addWidget(self.display_box_AGE_2, 3, 1, 1, 4)

        #       Regards the fifth row of the grid
        self.layout_grid_age.addWidget(self.display_box_AGE, 4, 1, 1, 4)

        #       Regards the sixth row of the grid
        self.layout_grid_age.addWidget(self.symbol_box_AGE, 6, 1, 1, 4)

    #   FOR THE TIME CALCULATOR MODE
    def _QLineEdit_time_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_TIME = QFont()
        font_symbol_box_TIME = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_TIME' attribute
        font_display_box_TIME.setPointSize(font_display_box_TIME.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_TIME' attribute
        font_symbol_box_TIME.setPointSize(font_symbol_box_TIME.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Time

        self.display_box_TIME.setReadOnly(False)
        self.display_box_TIME.setAlignment(Qt.AlignRight)
        self.display_box_TIME.setMaxLength(25)
        self.display_box_TIME.setFont(font_display_box_TIME)

        self.symbol_box_TIME.setFont(font_symbol_box_TIME)
        self.symbol_box_TIME.setMaxLength(25)
        self.symbol_box_TIME.setAlignment(Qt.AlignRight)
        self.symbol_box_TIME.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_time_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_time.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_time.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_time_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Time buttons
        self.button_FirstTime.setFont(self.font_button)
        self.button_SecondTime.setFont(self.font_button)
        self.button_CalculateTime.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Time buttons
        self.button_FirstTime.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondTime.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_CalculateTime.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_time(self):
        # -- Our 'Discount' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_time.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_time.addWidget(self.display_box_TIME, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_time.addWidget(self.symbol_box_TIME, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_time.addWidget(self.button_FirstTime, 4, 1)
        self.layout_grid_time.addWidget(self.button_SecondTime, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_time.addWidget(self.button_CalculateTime, 6, 2)

    #   FOR THE BMI CALCULATOR MODE
    def _QLineEdit_bmi_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_BMI = QFont()
        font_display_box_BMI_2 = QFont()
        font_symbol_box_BMI = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_BMI' attribute
        font_display_box_BMI.setPointSize(font_display_box_BMI.pointSize() + 10)
        # For the QLineEdit 'font_display_box_BMI_2' attribute
        font_display_box_BMI_2.setPointSize(font_display_box_BMI_2.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_TIME' attribute
        font_symbol_box_BMI.setPointSize(font_symbol_box_BMI.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- BMI

        self.display_box_BMI.setReadOnly(False)
        self.display_box_BMI.setAlignment(Qt.AlignRight)
        self.display_box_BMI.setMaxLength(25)
        self.display_box_BMI.setFont(font_display_box_BMI)

        self.display_box_BMI_2.setReadOnly(False)
        self.display_box_BMI_2.setAlignment(Qt.AlignRight)
        self.display_box_BMI_2.setMaxLength(25)
        self.display_box_BMI_2.setFont(font_display_box_BMI_2)

        self.symbol_box_BMI.setFont(font_symbol_box_BMI)
        self.symbol_box_BMI.setMaxLength(100)
        self.symbol_box_BMI.setAlignment(Qt.AlignRight)
        self.symbol_box_BMI.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_bmi_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_bmi.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_bmi.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_bmi_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * BMI buttons
        self.button_FirstBMI.setFont(self.font_button)
        self.button_CalculateBMI.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * BMI buttons
        self.button_CalculateBMI.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_FirstBMI.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_bmi(self):
        # -- Our 'BMI' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_bmi.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_bmi.addWidget(self.display_box_BMI, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_bmi.addWidget(self.display_box_BMI_2, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid_bmi.addWidget(self.button_FirstBMI, 3, 1)
        self.layout_grid_bmi.addWidget(self.button_CalculateBMI, 3, 2)

        #       Regards the fourth row of the grid
        self.layout_grid_bmi.addWidget(self.symbol_box_BMI, 4, 1, 1, 4)

    #   FOR THE LENGTH CALCULATOR MODE
    def _QLineEdit_length_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_LEN = QFont()
        font_symbol_box_LEN = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_LEN' attribute
        font_display_box_LEN.setPointSize(font_display_box_LEN.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_LEN' attribute
        font_symbol_box_LEN.setPointSize(font_symbol_box_LEN.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Length

        self.display_box_LEN.setReadOnly(False)
        self.display_box_LEN.setAlignment(Qt.AlignRight)
        self.display_box_LEN.setMaxLength(25)
        self.display_box_LEN.setFont(font_display_box_LEN)

        self.symbol_box_LEN.setFont(font_symbol_box_LEN)
        self.symbol_box_LEN.setMaxLength(25)
        self.symbol_box_LEN.setAlignment(Qt.AlignRight)
        self.symbol_box_LEN.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_length_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_length.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_length.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_length_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Length buttons
        self.button_CalculateLength.setFont(self.font_button)
        self.button_FirstLength.setFont(self.font_button)
        self.button_SecondLength.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Length buttons
        self.button_CalculateLength.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_FirstLength.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondLength.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_length(self):
        # -- Our 'Length' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_length.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_length.addWidget(self.display_box_LEN, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_length.addWidget(self.symbol_box_LEN, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_length.addWidget(self.button_FirstLength, 4, 1)
        self.layout_grid_length.addWidget(self.button_SecondLength, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_length.addWidget(self.button_CalculateLength, 6, 2)

    #   FOR THE MASS CALCULATOR MODE
    def _QLineEdit_mass_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_MASS = QFont()
        font_symbol_box_MASS = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_MASS' attribute
        font_display_box_MASS.setPointSize(font_display_box_MASS.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_MASS' attribute
        font_symbol_box_MASS.setPointSize(font_symbol_box_MASS.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Mass

        self.display_box_MASS.setReadOnly(False)
        self.display_box_MASS.setAlignment(Qt.AlignRight)
        self.display_box_MASS.setMaxLength(25)
        self.display_box_MASS.setFont(font_display_box_MASS)

        self.symbol_box_MASS.setFont(font_symbol_box_MASS)
        self.symbol_box_MASS.setMaxLength(25)
        self.symbol_box_MASS.setAlignment(Qt.AlignRight)
        self.symbol_box_MASS.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_mass_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_mass.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_mass.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_mass_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Mass buttons
        self.button_CalculateMass.setFont(self.font_button)
        self.button_FirstMass.setFont(self.font_button)
        self.button_SecondMass.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Mass buttons
        self.button_CalculateMass.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_FirstMass.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondMass.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def _QGridLayout_mass(self):
        # -- Our 'Mass' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_mass.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_mass.addWidget(self.display_box_MASS, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_mass.addWidget(self.symbol_box_MASS, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_mass.addWidget(self.button_FirstMass, 4, 1)
        self.layout_grid_mass.addWidget(self.button_SecondMass, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_mass.addWidget(self.button_CalculateMass, 6, 2)

    #   FOR THE SPEED CALCULATOR MODE
    def _QLineEdit_speed_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_SPEED = QFont()
        font_symbol_box_SPEED = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_SPEED' attribute
        font_display_box_SPEED.setPointSize(font_display_box_SPEED.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_SPEED' attribute
        font_symbol_box_SPEED.setPointSize(font_symbol_box_SPEED.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        # -- Speed

        self.display_box_SPEED.setReadOnly(False)
        self.display_box_SPEED.setAlignment(Qt.AlignRight)
        self.display_box_SPEED.setMaxLength(25)
        self.display_box_SPEED.setFont(font_display_box_SPEED)

        self.symbol_box_SPEED.setFont(font_symbol_box_SPEED)
        self.symbol_box_SPEED.setMaxLength(25)
        self.symbol_box_SPEED.setAlignment(Qt.AlignRight)
        self.symbol_box_SPEED.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_speed_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_speed.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_speed.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_speed_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Speed buttons
        self.button_CalculateSpeed.setFont(self.font_button)
        self.button_FirstSpeed.setFont(self.font_button)
        self.button_SecondSpeed.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Speed buttons
        self.button_CalculateSpeed.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_FirstSpeed.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondSpeed.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_speed(self):
        # -- Our 'Speed' QGridLayout --
        self.layout_grid_speed = QGridLayout()

        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_speed.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_speed.addWidget(self.display_box_SPEED, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_speed.addWidget(self.symbol_box_SPEED, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_speed.addWidget(self.button_FirstSpeed, 4, 1)
        self.layout_grid_speed.addWidget(self.button_SecondSpeed, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_speed.addWidget(self.button_CalculateSpeed, 6, 2)

    #   FOR THE DATA CALCULATOR MODE
    def _QLineEdit_data_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_DATA = QFont()
        font_symbol_box_DATA = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'font_display_box_DATA' attribute
        font_display_box_DATA.setPointSize(font_display_box_DATA.pointSize() + 10)
        # For the QLineEdit 'font_symbol_box_DATA' attribute
        font_symbol_box_DATA.setPointSize(font_symbol_box_DATA.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        self.display_box_DATA.setReadOnly(False)
        self.display_box_DATA.setAlignment(Qt.AlignRight)
        self.display_box_DATA.setMaxLength(25)
        self.display_box_DATA.setFont(font_display_box_DATA)

        self.symbol_box_DATA.setFont(font_symbol_box_DATA)
        self.symbol_box_DATA.setMaxLength(25)
        self.symbol_box_DATA.setAlignment(Qt.AlignRight)
        self.symbol_box_DATA.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_data_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_data.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_data.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_data_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Data buttons
        self.button_CalculateData.setFont(self.font_button)
        self.button_FirstData.setFont(self.font_button)
        self.button_SecondData.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Data buttons
        self.button_CalculateData.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_FirstData.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SecondData.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_data(self):
        # -- Our 'Data' QGridLayout --
        self.layout_grid_data = QGridLayout()

        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_data.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid_data.addWidget(self.display_box_DATA, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid_data.addWidget(self.symbol_box_DATA, 2, 1, 1, 4)

        #       Regards the fourth row of the grid
        self.layout_grid_data.addWidget(self.button_FirstData, 4, 1)
        self.layout_grid_data.addWidget(self.button_SecondData, 4, 3)

        #       Regards the sixth row of the grid
        self.layout_grid_data.addWidget(self.button_CalculateData, 6, 2)

    #   FOR THE DISCOUNT CALCULATOR MODE
    def _QLineEdit_discount_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box_DISC = QFont()
        font_display_box_DISC_2 = QFont()
        font_symbol_box_DISC = QFont()
        # ---------------------------------------------------------
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------
        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box_DISC' attribute
        font_display_box_DISC.setPointSize(font_display_box_DISC.pointSize() + 10)
        # For the QLineEdit 'display_box_DISC_2' attribute
        font_display_box_DISC_2.setPointSize(font_display_box_DISC_2.pointSize() + 10)
        # For the QLineEdit 'symbol_box_DISC' attribute
        font_symbol_box_DISC.setPointSize(font_symbol_box_DISC.pointSize() + 1)
        # ---------------------------------------------------------------------------
        # -- Changing some QLineEdit attributes through their functions
        self.display_box_DISC.setReadOnly(False)
        self.display_box_DISC.setAlignment(Qt.AlignRight)
        self.display_box_DISC.setMaxLength(25)
        self.display_box_DISC.setFont(font_display_box_DISC)
        self.display_box_DISC_2.setReadOnly(False)
        self.display_box_DISC_2.setAlignment(Qt.AlignRight)
        self.display_box_DISC_2.setMaxLength(25)
        self.display_box_DISC_2.setFont(font_display_box_DISC_2)
        self.symbol_box_DISC.setFont(font_symbol_box_DISC)
        self.symbol_box_DISC.setMaxLength(25)
        self.symbol_box_DISC.setAlignment(Qt.AlignRight)
        self.symbol_box_DISC.setReadOnly(True)
        # -------------------------------------------------------------

    def _QGridLayout_discount_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid_discount.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_discount.setSpacing(1.8)
        # --------------------------------------------

    def _QPushButton_discount_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        self.font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()
        # For the QPushButton 'button(s)' attributes
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------
        #       * Discount buttons
        self.button_CalculateDiscount.setFont(self.font_button)
        # ------------------------------------------------------------------
        # -- Assigning a size policy to our QPushButton attributes --
        #       * Discount buttons
        self.button_CalculateDiscount.setSizePolicy(
            QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

    def _QGridLayout_discount(self):
        # -- Our 'Discount' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid_discount.addWidget(self.menu_bar, 0, 1, 1, 4)
        #       Regards the third row of the grid
        self.layout_grid_discount.addWidget(self.display_box_DISC, 3, 1, 1, 4)
        #       Regards the fourth row of the grid
        self.layout_grid_discount.addWidget(self.display_box_DISC_2, 4, 1, 1, 4)
        #       Regards the fifth row of the grid
        self.layout_grid_discount.addWidget(self.button_CalculateDiscount, 5, 4)
        #       Regards the sixth row of the grid
        self.layout_grid_discount.addWidget(self.symbol_box_DISC, 6, 1, 1, 4)

    #   FOR THE SCIENTIFIC CALCULATOR MODE
    def _QLineEdit_scientific_properties(self):
        # -- Creating QFont attributes for the QLineEdit attributes
        font_display_box = QFont()
        font_symbol_box = QFont()
        # ---------------------------------------------------------

        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------

        # -- Assigning the QFont attributes to the corresponding QLineEdit attributes
        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 10)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 1)
        # ---------------------------------------------------------------------------

        # -- Changing some QLineEdit attributes through their functions
        self.display_box.setReadOnly(False)
        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(1000)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(250)
        self.symbol_box.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_scientific_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's & QLineEdit's attributes font
        font_button = QFont()
        font_symbol = QFont()
        font_extra = QFont()

        # For the QPushButton 'button(s)' attributes
        font_button.setPointSize(font_button.pointSize() + 6)
        # For the QPushButton 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 6)
        font_extra.setPointSize(font_extra.pointSize() + 2)
        # ---------------------------------------------------

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
        self.layout_grid_scientific.addWidget(self.button_times, 6, 5)

        #       Regards the seventh row of the grid
        self.layout_grid_scientific.addWidget(self.button_factorial, 7, 1)
        self.layout_grid_scientific.addWidget(self.button_minus, 7, 5)

        #       Regards the eighth row of the grid
        self.layout_grid_scientific.addWidget(self.button_inverse, 8, 1)
        self.layout_grid_scientific.addWidget(self.button_plus, 8, 5)

        #       Regards the ninth row of the grid
        self.layout_grid_scientific.addWidget(self.button_left_bracket, 9, 1)
        self.layout_grid_scientific.addWidget(self.button_right_bracket, 9, 2)
        self.layout_grid_scientific.addWidget(self.button_dot, 9, 4)
        self.layout_grid_scientific.addWidget(self.button_equal, 9, 5)
        # ------------------------------

    # ** GLOBAL CLASS SIGNALS & EVENTS **
    def Dark_Theme(self):
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------

    def Light_Theme(self):
        # -- Creating and setting the properties for the Color Palette
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.palette.setColor(QPalette.Text, Qt.white)
        self.palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.palette.setColor(QPalette.Highlight, QColor(25, 25, 25))
        self.palette.setColor(QPalette.HighlightedText, Qt.gray)
        self.setPalette(self.palette)
        # -------------------------------------------------------------

    def _QMenuBar_properties(self):
        # -- Assigning our attributes to the QMenuBar --
        self.menu_options = self.menu_bar.addMenu('Options')
        self.menu_settings = self.menu_bar.addMenu('Settings')
        self.menu_help = self.menu_bar.addMenu('Help')
        # ----------------------------------------------

        # -- Creating QAction attributes and connecting them to the menu attributes
        #       Regards the 'self.menu_options' attribute
        self.menu_options_overhead_name = QAction('Calculator Modes')
        self.menu_options_overhead_name.setSeparator(True)

        self.menu_options_modes_act = QAction('Modes')
        self.menu_options_modes_act.setShortcut('Ctrl+M')
        self.menu_options_modes_act.setChecked(True)

        #       Regards the 'self.menu_settings' attribute
        self.menu_settings_themes_act = QAction('Themes')
        self.menu_settings_themes_act.setShortcut('Ctrl+T')
        self.menu_settings_themes_act.setChecked(True)

        #       Regards the 'self.menu_help' attribute
        self.menu_help_about_act = QAction('About')
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

    def _QMenuBar_global_signals(self):
        # -- Calling our corresponding signal functions --
        #       Regards the 'self.menu_options' attribute
        self.menu_options_modes_act.triggered.connect(self._Mode_Change)
        #       Regards the 'self.menu_settings' attribute
        self.menu_settings_themes_act.triggered.connect(self._Theme_Change)

        #       Regards the 'self.menu_help' attribute
        self.menu_help_about_act.triggered.connect(self.clicked_help_about)
        # ------------------------------------------------

    def _QPushButton_global_signals(self):
        # -- Calling our corresponding signal functions --
        #       * Algebraic buttons
        self.button_exponent.clicked.connect(self.pressed_button_exponent)
        self.button_raise.clicked.connect(self.pressed_button_raise)
        self.button_absolute.clicked.connect(self.pressed_button_absolute)
        self.button_sqrt.clicked.connect(self.pressed_button_sqrt)
        self.button_log.clicked.connect(self.pressed_button_log)
        self.button_ln.clicked.connect(self.pressed_button_ln)
        self.button_pi.clicked.connect(self.pressed_button_pi)
        self.button_factorial.clicked.connect(self.pressed_button_factorial)

        #       * Trigonometric buttons
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

        #        * Discount button signals/events
        self.button_CalculateDiscount.clicked.connect(self.pressed_CalculateDiscount)

        #        * Temperature button signals/events
        self.button_CalculateTemp.clicked.connect(self.pressed_CalculateTemp)

        #        * Data button signals/events
        self.button_CalculateData.clicked.connect(self.pressed_CalculateData)

        #        * Age button signals/events
        self.button_CalculateAge.clicked.connect(self.pressed_CalculateAge)

        #        * Time button signals/events
        self.button_CalculateTime.clicked.connect(self.pressed_CalculateTime)

        #        * BMI button signals/events
        self.button_CalculateBMI.clicked.connect(self.pressed_CalculateBMI)

        #        * Date button signals/events
        self.button_CalculateDATE.clicked.connect(self.pressed_CalculateDATE)

        #        * Length buttons signals/events
        self.button_CalculateLength.clicked.connect(self.pressed_CalculateLength)

        #        * Mass buttons signals/events
        self.button_CalculateMass.clicked.connect(self.pressed_CalculateMass)

        #        * Speed buttons signals/events
        self.button_CalculateSpeed.clicked.connect(self.pressed_CalculateSpeed)
        # ------------------------------------------------

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
        # --------------------------
        # ** DECLARATION & ALTERING OF THE STANDARD CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------
        # -- QGridLayout --
        self.layout_grid_standard = QGridLayout()
        self._QGridLayout_standard_properties()
        self._QGridLayout_standard()
        # -- QPushButton properties --
        self._Make_Num_Buttons()
        # ----------------------------
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
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_scientific = QGridLayout()
        self._QGridLayout_scientific_properties()
        self._QGridLayout_scientific()
        # --------------

        # -- QPushButton properties --
        self._Make_Num_Buttons('sc')
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_discount_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_discount = QGridLayout()
        self._QGridLayout_discount_properties()
        self._QGridLayout_discount()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_temperature_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_temperature = QGridLayout()
        self._QGridLayout_temperature_properties()
        self._QGridLayout_temperature()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_data_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_data = QGridLayout()
        self._QGridLayout_data_properties()
        self._QGridLayout_data()
        # --------------
        # ----------------------------
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

    def _QWidget_calculator_date(self):
        # -- Common attributes among calculator modes --
        self._calculator_modes_declarations()
        # ----------------------------------------------

        # -- QWidget attribute --
        self.widget_calculator_date = QWidget()
        # -----------------------

        # -- QLineEdit properties --
        self._QLineEdit_date_properties()
        # --------------------------

        # -- QPushButton properties --
        self._QPushButton_date_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_date = QGridLayout()
        self._QGridLayout_date_properties()
        self._QGridLayout_date()
        # --------------
        # ----------------------------
        self.widget_calculator_date.setLayout(self.layout_grid_date)
        # -----------------

        # -- QMainWindow Layout --
        QMainWindow.setCentralWidget(self, self.widget_calculator_date)
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

        # -- QPushButton properties --
        self._QPushButton_age_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_age = QGridLayout()
        self._QGridLayout_age_properties()
        self._QGridLayout_age()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_time_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_time = QGridLayout()
        self._QGridLayout_time_properties()
        self._QGridLayout_time()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_bmi_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_bmi = QGridLayout()
        self._QGridLayout_bmi_properties()
        self._QGridLayout_bmi()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_length_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_length = QGridLayout()
        self._QGridLayout_length_properties()
        self._QGridLayout_length()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_mass_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_mass = QGridLayout()
        self._QGridLayout_mass_properties()
        self._QGridLayout_mass()
        # --------------
        # ----------------------------
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

        # -- QPushButton properties --
        self._QPushButton_speed_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF THE SCIENTIFIC CALCULATOR LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid_speed = QGridLayout()
        self._QGridLayout_speed_properties()
        self._QGridLayout_speed()
        # --------------
        # ----------------------------
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

    def _Theme_Change(self):
        self.widget_Theme = QWidget()
        self.layout_grid_Theme = QGridLayout()
        self.menu_bar = QMenuBar()
        self.font_button = QFont()
        self.font_test_display_box = QFont()

        self._QMenuBar_properties()

        self.test_display_box_1 = QLineEdit('The text will look like this')
        self.test_display_box_2 = QLineEdit('Select this text to see highlighted colors')

        self.test_display_box_1.setReadOnly(True)
        self.test_display_box_2.setReadOnly(True)
        self.test_display_box_2.selectAll()

        self.button_background_color = QPushButton('Background Color')
        self.button_text_color = QPushButton('Text Color')
        self.button_button_color = QPushButton('Background Color')
        self.button_display_color = QPushButton('Display Color')
        self.button_display_text = QPushButton('Display Text Color')
        self.button_reset_white_colors = QPushButton('Reset To Light Theme')
        self.button_reset_dark_colors = QPushButton('Reset To Dark Theme')

        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        self.font_test_display_box.setPointSize(self.font_test_display_box.pointSize() + 10)

        self.test_display_box_1.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.test_display_box_2.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_background_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_text_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_button_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_display_color.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_display_text.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_reset_white_colors.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_reset_dark_colors.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

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
        self.button_reset_white_colors.clicked.connect(self.Light_Theme)
        self.button_reset_dark_colors.clicked.connect(self.Dark_Theme)

        self.layout_grid_Theme.setContentsMargins(10, 12, 10, 10)
        self.layout_grid_Theme.setSpacing(10)

        self._QMenuBar_global_signals()

        self.widget_Theme.setLayout(self.layout_grid_Theme)
        QMainWindow.setCentralWidget(self, self.widget_Theme)

    def _Mode_Change(self):
        QWidget.setGeometry(self, 450, 210, 370, 310)
        self.widget_Mode = QWidget()
        self.layout_grid_Mode = QGridLayout()
        self.menu_bar = QMenuBar()
        self.font_button = QFont()

        self._QMenuBar_properties()

        #       * Modes buttons
        self.button_STANDARD = QPushButton(QIcon('assets/calc.png'), "STANDARD")
        self.button_SCIENTIFIC = QPushButton("SCIENTIFIC")
        self.button_BMI = QPushButton(QIcon('assets/bmi.png'), "BMI")
        self.button_AGE = QPushButton(QIcon('assets/age.png'), "AGE")
        self.button_TIME = QPushButton(QIcon('assets/clock.png'), "TIME")
        self.button_DATE = QPushButton(QIcon('assets/date.png'), "DATE")
        self.button_DATA = QPushButton(QIcon('assets/data.png'), "DATA")
        self.button_DISCOUNT = QPushButton(QIcon('assets/discount.png'), "DISCOUNT")
        self.button_LENGTH = QPushButton(QIcon('assets/length.png'), "LENGTH")
        self.button_MASS = QPushButton(QIcon('assets/mass.png'), "MASS")
        self.button_SPEED = QPushButton(QIcon('assets/speed.png'), "SPEED")
        self.button_TEMPERATURE = QPushButton(QIcon('assets/temperature.png'), "TEMPERATURE")

        self.font_button.setPointSize(self.font_button.pointSize() + 6)

        #       * Modes buttons
        self.button_STANDARD.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_SCIENTIFIC.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_BMI.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_AGE.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_DATA.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_DATE.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
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
        self.layout_grid_Mode.addWidget(self.button_DATE, 2, 2)
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
        self.button_DATE.clicked.connect(self.pressed_DATE)
        self.button_SCIENTIFIC.clicked.connect(self.pressed_SCIENTIFIC)

        self.layout_grid_Mode.setContentsMargins(10, 12, 4, 10)
        self.layout_grid_Mode.setSpacing(6)
        self._QMenuBar_global_signals()

        self.widget_Mode.setLayout(self.layout_grid_Mode)
        QMainWindow.setCentralWidget(self, self.widget_Mode)

    # ** CALCULATOR FUNCTIONS **
    def _calculate_invoked(self, function_called):
        # -- Displaying to the console --
        print("calculate has been invoked from", function_called)
        # -------------------------------

        # -- Making the necessary assignments --
        # Handling them locally so as to not affect any of the 'self' attributes
        local_string_last_number_used = self.string_last_number_used
        local_string_symbol_box = self.string_symbol_box
        if local_string_last_number_used == local_string_symbol_box:
            return local_string_last_number_used
        else:
            print('hey', local_string_symbol_box)
            return local_string_symbol_box
        # --------------------------------------

    def _update_string_attributes(self, symbol):
        # To be used inside symbol function (except equal) signals/events
        self.string_last_operand_used = symbol
        self.string_last_number_used = ''
        self.string_display_box = self.display_box.text()
        self.string_symbol_box = self.symbol_box.text()
        self.string_result += self.string_symbol_box + self.string_symbol_box

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
        # -- Setting the standard Theme --
        self.Dark_Theme()
        # -------------------------

    @Slot()
    # -- Slots & signals functions --
    # ** NUMBER BUTTONS SIGNALS **
    def NumButton_call(self, name):
        # Displaying to the console, so we know the key has been pressed
        print(name, "NumButton has been called")

        def numfunction():
            # -- Displaying to the console --
            print(name, 'has been pressed')
            # -------------------------------

            # -- If equal was last called, clear the 'display_box'
            if self.bool_equal_last_pressed:
                self.display_box.clear()
                self.bool_equal_last_pressed = False
            # ---------------------------------------------------

            # -- Prevents the user from typing in the display box 01 or 02 etc. --
            if name != '0' and self.display_box.text() == '0':
                self.display_box.clear()

            # -- Handing the input/output for the UI --
            # If another operand has not been pressed
            if self.bool_waiting_for_operand or self.bool_dont_del:
                self.bool_dont_del = False
                self.display_box.setText(self.display_box.text() + name)
            # Else clear the 'display_box' and add '0' to it
            else:
                self.display_box.clear()
                self.display_box.setText(self.display_box.text() + name)

            # -- If 0 is already on the 'display_box' keep it 0 --
            if self.display_box.text() == '00':
                self.display_box.setText('0')
            # -------------------------------------------------

            # Updating our string attribute(s)
            self.string_display_box = self.display_box.text()
            self.string_last_number_used += name

            # Resetting the operand flag(s)
            self.bool_waiting_for_operand = True
            # -----------------------------------------
        return numfunction

    # ** ALGEBRAIC BUTTONS **
    def pressed_button_exponent(self):
        # -- Displaying to the console --
        print('x² has been pressed')
        # -------------------------------

        if (self.bool_waiting_for_operand or not self.bool_equal_last_pressed) and self.display_box.text() != '':
            self.display_box.setText(self.display_box.text()+'**2')
            self.bool_waiting_for_operand = False

        if self.bool_equal_last_pressed:
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

    def pressed_button_raise(self):
        # -- Displaying to the console --
        print('xⁿ has been pressed')
        # -------------------------------

        if (self.bool_waiting_for_operand or not self.bool_equal_last_pressed) and self.display_box.text() != '':
            self.display_box.setText(self.display_box.text()+'**')
            self.bool_waiting_for_operand = False
            self.bool_dont_del = True

        if self.bool_equal_last_pressed:
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

    def pressed_button_absolute(self):
        # -- Displaying to the console --
        print('|x| has been pressed')
        # -------------------------------

        self.string_symbol_box = 'abs(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_sqrt(self):
        # -- Displaying to the console --
        print('√ has been pressed')
        # -------------------------------

        self.string_symbol_box = 'sqrt(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_log(self):
        # -- Displaying to the console --
        print('log has been pressed')
        # -------------------------------

        self.string_symbol_box = 'log10(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_ln(self):
        # -- Displaying to the console --
        print('ln has been pressed')
        # -------------------------------

        self.string_symbol_box = 'log(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_pi(self):
        # -- Displaying to the console --
        print('π has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
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
        # -- its important to not get the right numbers deleted if u have pressed π dont question it --
        if not keep:
            st = ''

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.clear()

        self.display_box.setText(st + str(math.pi))

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += str(math.pi)

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_button_factorial(self):
        # -- Displaying to the console --
        print('n! has been pressed')
        # -------------------------------

    def pressed_button_modular(self):
        # NOT DONE YET
        # -- Displaying to the console --
        print('% has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------
        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '+') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '%':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '+' in last operands' place and returning
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
            print(self.display_box.text())
            self.display_box.clear()
            print(self._calculate_invoked('%'))
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
        print('% has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(ne.evaluate(self._calculate_invoked('/'))))

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '/')

            # Updating the string attribute(s)
            self.string_last_operand_used = '/'
            self._update_string_attributes('/')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_division_last_pressed = True
            return
        # -----------------------------------------

    # ** TRIGONOMETRIC BUTTON SIGNALS **
    def pressed_button_sin(self):
        # -- Displaying to the console --
        print('sin has been pressed')
        # -------------------------------

        self.string_symbol_box = 'sin(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_cos(self):
        # -- Displaying to the console --
        print('cos has been pressed')
        # -------------------------------

        self.string_symbol_box = 'cos(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    def pressed_button_tan(self):
        # -- Displaying to the console --
        print('tan has been pressed')
        # -------------------------------

        self.string_symbol_box = 'tan(' + self.display_box.text()

        self.symbol_box.setText(self.symbol_box.text() + self.string_symbol_box)

        self.bool_dont_del = False

        self.left_bracket_count += 1

    # ** OPERAND BUTTONS SIGNALS **
    def pressed_button_equal(self):
        # -- Displaying to the console --
        print('= has been pressed')
        # -------------------------------

        if self.display_box.text() == '':
            return

        add_brackets = self.left_bracket_count - self.right_bracket_count

        for i in range(add_brackets):
            self.display_box.setText(self.display_box.text() + ')')

        self.left_bracket_count = 0
        self.right_bracket_count = 0

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
        self.display_box.setText(str(ne.evaluate(self.string_result))
                            )# Clearing the 'symbol_box' and its corresponding string ('string_symbol_box') attribute
        self.string_symbol_box = ''

        # Resetting the operand flag(s)
        self._reset_symbol_flags()
        self.bool_waiting_for_operand = True
        self.bool_equal_last_pressed = True
        # -----------------------------------------

    def pressed_button_plus(self):
        # -- Displaying to the console --
        print('+ has been pressed')
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
            add_brackets = self.left_bracket_count - self.right_bracket_count

            for i in range(add_brackets):
                self.display_box.setText(self.display_box.text() + ')')
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()
            # Clearing the 'display_box' in the process
            print(self.display_box.text())
            self.display_box.clear()
            print(self._calculate_invoked('+'))
            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(str(ne.evaluate(self._calculate_invoked('+')))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

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
        print('- has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------

        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '+') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '-':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '+' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '-')
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
            print(self.display_box.text())
            self.display_box.clear()
            print(self._calculate_invoked('-'))
            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(ne.evaluate((self._calculate_invoked('-')))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

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
        print('* has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text():
            return
        # --------------------------------------------------------------------------------

        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '+') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '*':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '+' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '*')
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
            print(self.display_box.text())
            self.display_box.clear()
            print(self._calculate_invoked('*'))
            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(ne.evaluate(self._calculate_invoked('*'))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

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
        print('/ has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if self.display_box.text() == '' or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

        if self.left_bracket_count == self.right_bracket_count:
            # -- If another operand (other than '+') has been called replace it --
            if not self.bool_waiting_for_operand and self.string_last_operand_used != '/':
                # Assigning the contents of the 'symbol_box' to its corresponding string attribute
                self.string_symbol_box = self.symbol_box.text()

                # Removing the current operand
                self.string_symbol_box = self.string_symbol_box[:-1]

                # Putting '+' in last operands' place and returning
                self.symbol_box.setText(self.string_symbol_box + '/')
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

            if str(str(ne.evaluate(self._calculate_invoked('/')))) == '0':
                for i in range(add_brackets):
                    self.string_symbol_box = self.string_symbol_box[:-1]
                return

            # Clearing the 'display_box' in the process
            print(self.display_box.text())
            self.display_box.clear()
            print(self._calculate_invoked('/'))
            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(ne.evaluate(self._calculate_invoked('/'))))

            add_brackets = self.left_bracket_count - self.right_bracket_count

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

    # ** SYMBOL BUTTONS SIGNALS **
    def pressed_button_clear_entry(self):
        # -- Displaying to the console --
        print('CE has been pressed')
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

        if self.symbol_box.text():
            self.bool_dont_del = False
            self.bool_waiting_for_operand = False
            self.bool_equal_last_pressed = False
            self._reset_symbol_flags()

        # --------------------------------------

    def pressed_button_clear(self):
        # -- Displaying to the console --
        print('C has been pressed')
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
        self.bool_dont_del = False
        self.bool_waiting_for_operand = False
        self.bool_equal_last_pressed = False
        self._reset_symbol_flags()
        # --------------------------------------

    def pressed_button_backspace(self):
        # -- Displaying to the console --
        print('⌫ has been pressed')
        # -------------------------------

        st = self.display_box.text()

        if len(st)>1:
            if st[-1] == ')':
                self.right_bracket_count -= 1

            if st[-1] == '(':
                self.left_bracket_count -= 1

        if len(st) > 3:
            if st[-1] == '2' and st[-2] == '*' and st[-3] == '*':
                self.bool_dont_del = True

        # -- Handing the input/output for the UI --
        st = st[:-1]
        self.display_box.setText(st)

        # If the 'display_box' is empty
        if not self.display_box.text():
            self.bool_waiting_for_operand = False
        # -----------------------------------------

    def pressed_button_inverse(self):
        # -- Displaying to the console --
        print('+/- has been pressed')
        # -------------------------------

        # -- If 0 is already on the 'display_box' return --
        if self.display_box.text() == '0':
            print("-0 Doesn't exist, i think")
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
        print('. has been pressed')
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
        print('( has been pressed')
        # -------------------------------
        if not self.bool_dont_del:
            self.display_box.clear()

        self.left_bracket_count = self.left_bracket_count + 1
        self.bool_dont_del = True
        self.bool_equal_last_pressed = False
        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + '(')
        # -----------------------------------------

    def pressed_button_right_bracket(self):
        # -- Displaying to the console --
        print(') has been pressed')
        # -------------------------------

        if self.left_bracket_count < self.right_bracket_count or self.left_bracket_count == '0':
            print('Error: Cant add ) withought enough ( before')
            return

        self.right_bracket_count = self.right_bracket_count + 1
        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + ')')
        # -----------------------------------------

    # ** MENU & ACTION SIGNALS **
    def pressed_SCIENTIFIC(self):
        # -- Displaying to the console --
        print('scientific has been pressed')
        # -------------------------------
        self._QWidget_calculator_scientific()
        self.pressed_button_clear()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_TIME(self):
        print("Time button has been pressed")
        # -------------------------------
        self._QWidget_calculator_time()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_MASS(self):
        print("Mass button has been pressed")
        # -------------------------------
        self._QWidget_calculator_mass()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_AGE(self):
        print("Age button has been pressed")
        # -------------------------------
        self._QWidget_calculator_age()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_DATE(self):
        print("Date button has been pressed")
        # -------------------------------
        self._QWidget_calculator_date()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_DATA(self):
        print("Data button has been pressed")
        # -------------------------------
        self._QWidget_calculator_data()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_LENGTH(self):
        print("Length button has been pressed")
        # -------------------------------
        self._QWidget_calculator_length()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_TEMPERATURE(self):
        print("Temperature button has been pressed")
        # -------------------------------
        self._QWidget_calculator_temperature()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_SPEED(self):
        print("Speed button has been pressed")
        # -------------------------------
        self._QWidget_calculator_speed()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_DISCOUNT(self):
        print("Discount button has been pressed")
        # -------------------------------
        self._QWidget_calculator_discount()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_BMI(self):
        print("BMI button has been pressed")
        # -------------------------------
        self._QWidget_calculator_bmi()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_STANDARD(self):
        print("Standard button has been pressed")
        # -------------------------------
        self._QWidget_calculator_standard()
        self.pressed_button_clear()
        self.bool_temp_modes = True
        # ------------------------------------

    def pressed_CalculateAge(self):
        print("Your age is...")

    def pressed_CalculateBMI(self):
        print("Your BMI is...")
        if self.button_FirstBMI.currentIndex() == 0:
            bmi = str(ne.evaluate('(' + self.display_box_BMI.text()+')/('
                                                        + self.display_box_BMI_2.text()+'/100) ** 2'))
        else:
            bmi = str(ne.evaluate('(' + self.display_box_BMI.text() + '/'
                                                        + self.display_box_BMI_2.text() + '/'
                                                        + self.display_box_BMI_2.text() + ')*703'))


        BMI = float(bmi)

        BMI = float("{:.2}".format(BMI))

        if BMI <= 18.4:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are underweight.")
        elif BMI <= 24.9:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are healthy.")
        elif BMI <= 29.9:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are over weight.")
        elif BMI <= 34.9:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are severely over weight.")
        elif BMI <= 39.9:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are obese.")
        elif BMI > 39.9:
            self.symbol_box_BMI.setText("Your BMI is " + str(BMI) + ".You are severely obese.")

    def pressed_CalculateTime(self):
        print("Hah im awesome after all")

    def pressed_CalculateDATE(self):
        print("")

    def pressed_CalculateData(self):
        print("This works too owo")

    def pressed_CalculateDiscount(self):
        print("")

    def pressed_CalculateLength(self):
        print("I can't take any more of my awesomeness")

    def pressed_CalculateMass(self):
        print("Holy shit I'm on fire dawg")

    def pressed_CalculateTemp(self):
        print("Hey it works")

    def pressed_CalculateSpeed(self):
        print("Hell yeah :)")

    def pressed_button_background_color(self):
        # -- Displaying to the console --
        print('Background color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title="Choose Background Color")
        self.palette.setColor(QPalette.Window, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_text_color(self):
        # -- Displaying to the console --
        print('Text color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Choose Text Color')
        self.palette.setColor(QPalette.ButtonText, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_color(self):
        # -- Displaying to the console --
        print('Button color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Choose Button Color')
        self.palette.setColor(QPalette.Button, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_display_color(self):
        # -- Displaying to the console --
        print('Display color has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title='Choose Display Color')
        self.palette.setColor(QPalette.Base, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def pressed_button_display_text(self):
        # -- Displaying to the console --
        print("Display text's color button has been pressed")
        # -------------------------------

        # -- Handing the input/output for the UI --
        color = QColorDialog.getColor(title="Choose Text Color")
        self.palette.setColor(QPalette.Text, color)
        color = QColorDialog.getColor(title="Choose Highlighted Text Color")
        self.palette.setColor(QPalette.HighlightedText, color)
        self.setPalette(self.palette)
        # -----------------------------------------

    def clicked_help_about(self):
        # -- Displaying to the console --
        print('About has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        print('Creators: Vasilis, Thanosks, Xarison, Panagos')
        # -----------------------------------------
    # -------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())

