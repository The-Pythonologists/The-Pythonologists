import sys

import sympy
from PySide6.QtGui import (QAction, QFont, QIcon, QKeyEvent)
from PySide6.QtCore import (Qt, Slot)
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton,
                               QSizePolicy, QMenuBar, QColorDialog)


class Calculator(QWidget):
    # ** CLASS PROPERTIES **
    def _QWidget_properties(self):
        # -- Assigning our QWidget's properties --
        QWidget.setWindowTitle(self, "Calculator")
        QWidget.setWindowIcon(self, QIcon('assets/calc_transparent.png'))
        QWidget.setGeometry(self, 450, 220, 330, 330)
        # --------------------------------------

    def _QLineEdit_properties(self):
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
        self.display_box.setMaxLength(25)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(25)
        self.symbol_box.setFont(font_symbol_box)
        # -------------------------------------------------------------

    def _QPushButton_properties(self):
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

        # -- Assigning our QFont attributes to our QPushButton attributes --
        #       * Number buttons
        self.button_num0.setFont(font_button)
        self.button_num1.setFont(font_button)
        self.button_num2.setFont(font_button)
        self.button_num3.setFont(font_button)
        self.button_num4.setFont(font_button)
        self.button_num5.setFont(font_button)
        self.button_num6.setFont(font_button)
        self.button_num7.setFont(font_button)
        self.button_num8.setFont(font_button)
        self.button_num9.setFont(font_button)

        #       * Operand buttons
        self.button_equal.setFont(font_symbol)
        self.button_plus.setFont(font_symbol)
        self.button_minus.setFont(font_symbol)
        self.button_times.setFont(font_symbol)
        self.button_division.setFont(font_symbol)

        #       * Symbol buttons
        self.button_clear_all.setFont(font_extra)
        self.button_clear.setFont(font_extra)
        self.button_backspace.setFont(font_extra)
        self.button_inverse.setFont(font_extra)
        self.button_dot.setFont(font_symbol)
        self.button_left_bracket.setFont(font_symbol)
        self.button_right_bracket.setFont(font_symbol)
        # ------------------------------------------------------------------

        # -- Assigning a size policy to our QPushButton attributes --
        #       * Number buttons
        self.button_num0.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num1.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num2.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num3.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num4.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num5.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num6.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num7.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num8.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num9.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #       * Operand buttons
        self.button_equal.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_plus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_minus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_times.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_division.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_modular.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #       * Symbol buttons
        self.button_clear_all.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_clear.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_backspace.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_inverse.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_dot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_left_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_right_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------------

        self.button_clear_all.setMinimumHeight(40)

    def _QMenuBar_properties(self):
        # NOT YET FINISHED, RE-WRITE DUDE
        # -- Assigning our attributes to the QMenuBar --
        self.menu_options = self.menu_bar.addMenu('Options')
        self.menu_settings = self.menu_bar.addMenu('Settings')
        self.menu_info = self.menu_bar.addMenu('Info')
        # ----------------------------------------------

        # -- Creating QAction attributes and connecting them to the corresponding signals
        self.menu_action0 = QAction('Themes')
        self.menu_action0.setSeparator(True)

        self.menu_action1 = QAction('Modes')
        self.menu_action1.setChecked(True)

        self.menu_action2 = QAction('Background Color')
        self.menu_action2.setShortcut('Ctrl+B')
        self.menu_action2.setChecked(True)

        self.menu_action3 = QAction('Text Color')
        self.menu_action3.setShortcut('Ctrl+T')
        self.menu_action3.setChecked(True)

        self.menu_action4 = QAction('Button Color')
        self.menu_action4.setShortcut('Shift+Ctrl+B')
        self.menu_action4.setChecked(True)

        self.menu_action5 = QAction('Display Color')
        self.menu_action5.setShortcut('Ctrl+D')
        self.menu_action5.setChecked(True)

        self.menu_action6 = QAction('Display Text Color')
        self.menu_action6.setShortcut('Shift+Ctrl+D')
        self.menu_action6.setChecked(True)

        self.menu_action7 = QAction('About the application')
        self.menu_action7.setChecked(True)
        # --------------------------------------------------------------------------------

        # -- Assigning our QActions to their corresponding attributes
        #       Regarding the settings
        #       Regarding the options
        self.menu_options.addAction(self.menu_action1)
        self.menu_settings.addAction(self.menu_action2)
        self.menu_settings.addAction(self.menu_action3)
        self.menu_info.addAction(self.menu_action4)
        #       Regarding the information
        # -----------------------------------------------------------

    def _QGridLayout_properties(self):
        # -- Assigning our QGridLayout's properties --
        self.layout_grid.setContentsMargins(10, 12, 10, 10)
        self.layout_grid.setSpacing(1.8)
        # --------------------------------------------

    # ** LAYOUT MODES **
    def _QGridLayout_standard(self):
        # -- Our 'Standard' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        #       Regards the QMenuBar and it's constant throughout the class
        self.layout_grid.addWidget(self.menu_bar, 0, 1, 1, 4)

        #       Regards the first row of the grid
        self.layout_grid.addWidget(self.symbol_box, 1, 1, 1, 4)

        #       Regards the second row of the grid
        self.layout_grid.addWidget(self.display_box, 2, 1, 1, 4)

        #       Regards the third row of the grid
        self.layout_grid.addWidget(self.button_clear_all, 3, 1)
        self.layout_grid.addWidget(self.button_clear, 3, 2)
        self.layout_grid.addWidget(self.button_backspace, 3, 3)
        self.layout_grid.addWidget(self.button_division, 3, 4)

        #       Regards the fourth row of the grid
        self.layout_grid.addWidget(self.button_num7, 4, 1)
        self.layout_grid.addWidget(self.button_num8, 4, 2)
        self.layout_grid.addWidget(self.button_num9, 4, 3)
        self.layout_grid.addWidget(self.button_times, 4, 4)

        #       Regards the fifth row of the grid
        self.layout_grid.addWidget(self.button_num4, 5, 1)
        self.layout_grid.addWidget(self.button_num5, 5, 2)
        self.layout_grid.addWidget(self.button_num6, 5, 3)
        self.layout_grid.addWidget(self.button_minus, 5, 4)

        #       Regards the sixth row of the grid
        self.layout_grid.addWidget(self.button_num1, 6, 1)
        self.layout_grid.addWidget(self.button_num2, 6, 2)
        self.layout_grid.addWidget(self.button_num3, 6, 3)
        self.layout_grid.addWidget(self.button_plus, 6, 4)

        #       Regards the seventh row of the grid
        self.layout_grid.addWidget(self.button_inverse, 7, 1)
        self.layout_grid.addWidget(self.button_num0, 7, 2)
        self.layout_grid.addWidget(self.button_dot, 7, 3)
        self.layout_grid.addWidget(self.button_equal, 7, 4)
        # ------------------------------

    def _QGridLayout_scientific(self):  # Yet to be declared and defined
        # -- Our 'Scientific' QGridLayout --
        # Adding our widgets (QLineEdit, QPushButton etc) to our QGridLayout
        self.layout_grid.addWidget(self.button_dot)  # Will change it later, leave is as is for now
        # ----------------------------------

    # ** CLASS SIGNALS & EVENTS **
    def _QMenuBar_signals(self):
        # -- Calling our corresponding signal functions --
        self.menu_action1.triggered.connect(self.clicked_modes)
        self.menu_action2.triggered.connect(self.clicked_background_color)
        self.menu_action3.triggered.connect(self.clicked_text_color)
        self.menu_action4.triggered.connect(self.clicked_info)
        # ------------------------------------------------

    def _QPushButton_signals(self):
        # -- Calling our corresponding signal functions --
        #       * Number button signals/events
        self.button_num0.clicked.connect(self.pressed_num0)
        self.button_num1.clicked.connect(self.pressed_num1)
        self.button_num2.clicked.connect(self.pressed_num2)
        self.button_num3.clicked.connect(self.pressed_num3)
        self.button_num4.clicked.connect(self.pressed_num4)
        self.button_num5.clicked.connect(self.pressed_num5)
        self.button_num6.clicked.connect(self.pressed_num6)
        self.button_num7.clicked.connect(self.pressed_num7)
        self.button_num8.clicked.connect(self.pressed_num8)
        self.button_num9.clicked.connect(self.pressed_num9)

        #       * Operand button signals/events
        self.button_equal.clicked.connect(self.pressed_button_equal)
        self.button_plus.clicked.connect(self.pressed_button_plus)
        self.button_minus.clicked.connect(self.pressed_button_minus)
        self.button_times.clicked.connect(self.pressed_button_times)
        self.button_division.clicked.connect(self.pressed_button_division)
        self.button_modular.clicked.connect(self.pressed_button_modular)

        #       * Symbol button signals/events
        self.button_clear_all.clicked.connect(self.pressed_button_clear_all)
        self.button_clear.clicked.connect(self.pressed_button_clear)
        self.button_backspace.clicked.connect(self.pressed_button_backspace)
        self.button_inverse.clicked.connect(self.pressed_button_inverse)
        self.button_dot.clicked.connect(self.pressed_button_dot)
        self.button_left_bracket.clicked.connect(self.pressed_button_left_bracket)
        self.button_right_bracket.clicked.connect(self.pressed_button_right_bracket)
        # ------------------------------------------------

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
        self._QWidget_properties()  # Setting the widget's properties
        # --------------------------

        # ** DECLARATION & ALTERING OF ATTRIBUTES **
        # -- Boolean attributes --
        self.bool_waiting_for_operand = False  # Set to False so it doesn't display a symbol that's pressed on its first run
        self.bool_equal_last_pressed = False  # To check whether the last symbol pressed was a '=' sign
        self.bool_plus_last_pressed = False  # To check whether the last symbol pressed was a '+' sign
        self.bool_minus_last_pressed = False  # To check whether the last symbol pressed was a '-' sign
        self.bool_times_last_pressed = False  # To check whether the last symbol pressed was a '*' sign
        self.bool_division_last_pressed = False  # To check whether the last symbol pressed was a '/' sign
        self.bool_modular_last_pressed = False  # To check whether the last symbol pressed was a 'Mod' sign
        # ------------------------

        # -- List attributes --
        self.list_symbols = ['+', '-', '*', '/']
        # ---------------------

        # -- String attributes --
        self.string_display_box = ''  # Contains the contents of the 'display_box'
        self.string_symbol_box = ''  # Contains the contents of the 'symbol_box'
        self.string_result = ''  # Contains the contents of the complete string
        self.string_last_operand_used = ''  # Contains the contents of the last operand used (excluding = operand)
        self.string_last_number_used = ''  # Contains the contents of the last number used
        self.string_calculated_invoked = ''  # Contains the contents of the function '_calculated_invoked'
        # -----------------------

        # -- QLineEdit attributes --
        self.display_box = QLineEdit('')
        self.symbol_box = QLineEdit('')
        self._QLineEdit_properties()
        # --------------------------

        # -- QPushButton attributes --
        #       * Number buttons
        self.button_num0 = QPushButton('0')
        self.button_num1 = QPushButton('1')
        self.button_num2 = QPushButton('2')
        self.button_num3 = QPushButton('3')
        self.button_num4 = QPushButton('4')
        self.button_num5 = QPushButton('5')
        self.button_num6 = QPushButton('6')
        self.button_num7 = QPushButton('7')
        self.button_num8 = QPushButton('8')
        self.button_num9 = QPushButton('9')
        #       * Operand buttons
        self.button_equal = QPushButton('=')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_times = QPushButton('*')
        self.button_division = QPushButton('/')
        self.button_modular = QPushButton('Mod')
        #       * Symbol buttons
        self.button_clear_all = QPushButton('CE')
        self.button_clear = QPushButton('C')
        self.button_backspace = QPushButton('⌫')
        self.button_inverse = QPushButton('+/-')
        self.button_dot = QPushButton('.')
        self.button_left_bracket = QPushButton('(')
        self.button_right_bracket = QPushButton(')')
        self._QPushButton_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF LAYOUT & MENU BAR **
        # -- QMenuBar --
        self.menu_bar = QMenuBar()
        self._QMenuBar_properties()
        # --------------

        # -- QGridLayout --
        self.layout_grid = QGridLayout()
        self._QGridLayout_properties()
        # We will change it later to respond to the menu presses
        if True:
            self._QGridLayout_standard()
        else:
            self._QGridLayout_scientific()  # Will change it later

        QWidget.setLayout(self, self.layout_grid)  # same as 'self.setLayout(self.layout_grid)'
        # -----------------

        # ** DECLARATION & ALTERING OF SIGNALS & EVENTS **
        # -- QMenuBar signals --
        self._QMenuBar_signals()
        # ----------------------

        # -- QPushButton signals --
        self._QPushButton_signals()
        # -------------------------

    @Slot()
    # -- Slots & signals functions --
    # ** NUMBER BUTTONS SIGNALS **
    def pressed_num0(self):
        # -- Displaying to the console --
        print('0 has been pressed')
        # -------------------------------

        # -- If 0 is already on the 'display_box' return --
        if self.display_box.text() == '0':
            return
        # -------------------------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '0')
        # Else clear the 'display_box' and add '0' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '0')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '0'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num1(self):
        # -- Displaying to the console --
        print('1 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '1')
        # Else clear the 'display_box' and add '1' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '1')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '1'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num2(self):
        # -- Displaying to the console --
        print('2 has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '2')
        # Else clear the 'display_box' and add '2' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '2')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '2'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num3(self):
        # -- Displaying to the console --
        print('3 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '3')
        # Else clear the 'display_box' and add '3' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '3')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '3'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num4(self):
        # -- Displaying to the console --
        print('4 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '4')
        # Else clear the 'display_box' and add '4' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '4')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '4'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num5(self):
        # -- Displaying to the console --
        print('5 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '5')
        # Else clear the 'display_box' and add '5' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '5')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '5'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num6(self):
        # -- Displaying to the console --
        print('6 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '6')
        # Else clear the 'display_box' and add '6' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '6')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '6'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num7(self):
        # -- Displaying to the console --
        print('7 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '7')
        # Else clear the 'display_box' and add '7' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '7')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '7'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num8(self):
        # -- Displaying to the console --
        print('8 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '8')
        # Else clear the 'display_box' and add '8' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '8')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '8'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    def pressed_num9(self):
        # -- Displaying to the console --
        print('9 has been pressed')
        # -------------------------------

        # -- If equal was last called, clear the 'display_box'
        if self.bool_equal_last_pressed:
            self.display_box.clear()
            self.bool_equal_last_pressed = False
        # ---------------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            self.display_box.setText(self.display_box.text() + '9')
        # Else clear the 'display_box' and add '0' to it
        else:
            self.display_box.clear()
            self.display_box.setText(self.display_box.text() + '9')

        # Updating our string attribute(s)
        self.string_display_box = self.display_box.text()
        self.string_last_number_used += '9'

        # Resetting the operand flag(s)
        self.bool_waiting_for_operand = True
        # -----------------------------------------

    # ** OPERAND BUTTONS SIGNALS **
    def pressed_button_equal(self):
        # -- Displaying to the console --
        print('= has been pressed')
        # -------------------------------

        # -- If another operand (other than '=') has been called return --
        if not self.bool_waiting_for_operand and not self.bool_equal_last_pressed:
            return
        # ----------------------------------------------------------------

        # -- If the last operand called was '=' calculate and return --
        if self.bool_equal_last_pressed:
            # Calculating the result and assigning it to the 'string_result' attribute
            self.string_result += self.string_last_operand_used + self.string_last_number_used

            # Clearing the contents of the 'string_symbol_box' and 'symbol_box' attributes
            self.string_symbol_box = ''  # Will use a 'string_history_box' later to hold it in
            self.symbol_box.clear()

            # Displaying the result to the 'display_box' attribute and return
            self.display_box.setText(str(sympy.sympify(self.string_result)))
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
        self.display_box.setText(str(sympy.sympify(self.string_result)))

        # Clearing the 'symbol_box' and its corresponding string ('string_symbol_box') attribute
        self.symbol_box.clear()
        self.string_symbol_box = ''
        # -----------------------------------------

        # Resetting the operand flag(s)
        self._reset_symbol_flags()
        self.bool_waiting_for_operand = True
        self.bool_equal_last_pressed = True

    def pressed_button_plus(self):
        # -- Displaying to the console --
        print('+ has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text() or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

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
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(sympy.sympify(self._calculate_invoked('+'))))

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '+')

            # Updating the string attribute(s)
            self.string_last_operand_used = '+'
            self._update_string_attributes('+')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_plus_last_pressed = True  # Will change it later, for leaving it as is for now
            return
        # -----------------------------------------

    def pressed_button_minus(self):
        # -- Displaying to the console --
        print('- has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text() or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

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
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(sympy.sympify(self._calculate_invoked('-'))))

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '-')

            # Updating the string attribute(s)
            self.string_last_operand_used = '-'
            self._update_string_attributes('-')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_minus_last_pressed = True  # Will change it later, for leaving it as is for now
            return
        # -----------------------------------------

    def pressed_button_times(self):
        # -- Displaying to the console --
        print('* has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text() or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

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
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(sympy.sympify(self._calculate_invoked('*'))))

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '*')

            # Updating the string attribute(s)
            self.string_last_operand_used = '*'
            self._update_string_attributes('*')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_times_last_pressed = True  # Will change it later, for leaving it as is for now
            return
        # -----------------------------------------

    def pressed_button_division(self):
        # -- Displaying to the console --
        print('/ has been pressed')
        # -------------------------------

        # -- If the 'display_box' is empty (or is equal to 0, the default value) return --
        if not self.display_box.text() or self.display_box.text() == '0':
            return
        # --------------------------------------------------------------------------------

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
            # Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()

            # Clearing the 'display_box' in the process
            self.display_box.clear()

            # Retain the last calculated or the last number used after clearing the 'display_box'
            self.display_box.setText(str(sympy.sympify(self._calculate_invoked('/'))))

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + '/')

            # Updating the string attribute(s)
            self.string_last_operand_used = '/'
            self._update_string_attributes('/')

            # Resetting the operand flag(s) and returning
            self._reset_symbol_flags()
            self.bool_waiting_for_operand = False
            self.bool_division_last_pressed = True  # Will change it later, for leaving it as is for now
            return
        # -----------------------------------------

    def pressed_button_modular(self):
        # Haven't changed it yet like the rest of the symbols
        # REFRAIN FROM USING FOR NOW, HAS NOT BEEN UPDATED
        # -- Displaying to the console --
        print('Mod has been pressed')
        # -------------------------------

        # -- If another operand has been called return --
        if not self.bool_waiting_for_operand:
            return
        # -----------------------------------------------

        # -- Handing the input/output for the UI --
        # If another operand has not been pressed
        if self.bool_waiting_for_operand:
            # Altering the necessary attributes
            # - Transferring the output of the 'display_box' to the 'string_symbol_box'
            self.string_symbol_box += self.display_box.text()
            # - Clearing the 'display_box' in the process
            self.display_box.clear()

            # Displaying to the corresponding QLineEdit attribute
            self.symbol_box.setText(self.string_symbol_box + 'Mod')

            # Resetting our 'waiting_for_operand' flag to False and our 'plus_last_pressed' to True
            self.bool_waiting_for_operand = False
            self._update_string_attributes('Mod')
            return
        # -----------------------------------------

        # -- Updating our string attributes --
        # This is in case it doesn't enter any of the if statements
        self.string_last_operand_used = 'Mod'
        self.string_last_number_used = ''
        self.string_display_box = self.display_box.text()
        self.string_symbol_box = self.symbol_box.text()
        self.string_result += self.string_symbol_box + self.string_symbol_box
        # ------------------------------------

        # Setting the operand flag to True so symbols can't be added on top of one another
        self.bool_waiting_for_operand = False
        self._reset_symbol_flags()

    # ** SYMBOL BUTTONS SIGNALS **
    def pressed_button_clear_all(self):
        # -- Displaying to the console --
        print('CE has been pressed')
        # -------------------------------

        # -- Updating and clearing attributes --
        self.display_box.clear()
        self.string_display_box = ''
        self.string_result = ''
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
        self.bool_waiting_for_operand = False
        self.bool_equal_last_pressed = False
        self._reset_symbol_flags()
        # --------------------------------------

    def pressed_button_backspace(self):
        # -- Displaying to the console --
        print('⌫ has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        st = self.display_box.text()
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

        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + '(')
        # -----------------------------------------

    def pressed_button_right_bracket(self):
        # -- Displaying to the console --
        print(') has been pressed')
        # -------------------------------

        # -- Handing the input/output for the UI --
        self.display_box.setText(self.display_box.text() + ')')
        # -----------------------------------------

    # ** MENU & ACTION SIGNALS **
    def clicked_modes(self):
        # -- Displaying to the console --
        print('Modes button has been pressed')
        # -------------------------------

    def clicked_text_color(self):
        # -- Displaying to the console --
        print('Text color has been pressed')
        # -------------------------------

    def clicked_background_color(self):
        # -- Displaying to the console --
        print('Background color button has been pressed')
        # -------------------------------

        color = QColorDialog.getColor()
        self.setStyleSheet('QWdiget {background-color: %s' % color.name())

    def clicked_info(self):
        # -- Displaying to the console --
        print('Info button has been pressed')
        # -------------------------------
    # -------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    widget = Calculator()
    widget.show()

    sys.exit(app.exec_())
