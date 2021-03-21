import sys

import sympy
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtCore import (Qt, Slot)
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QSizePolicy)


class Calculator(QWidget):
    def _QWidget_properties(self):
        QWidget.setWindowTitle(self, "Calculator")  # same as self.setWindowTitle("Calculator")
        QWidget.setGeometry(self, 450, 250, 250, 250)   # same as self.setGeometry(450, 250, 250, 250)

    def _QLineEdit_properties(self):
        # -- QFont attributes for the QLineEdit attributes --
        # To change QLineEdit's attributes font
        font_display_box = QFont()
        font_symbol_box = QFont()

        # For the QLineEdit 'display_box' attribute
        font_display_box.setPointSize(font_display_box.pointSize() + 8)
        # For the QLineEdit 'symbol_box' attribute
        font_symbol_box.setPointSize(font_symbol_box.pointSize() + 2)
        # ---------------------------------------------------

        # Assigning our QFont attributes to our QLineEdit attributes
        self.display_box.setReadOnly(True)
        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(15)
        self.display_box.setFont(font_display_box)

        self.symbol_box.setReadOnly(True)
        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(10)
        self.symbol_box.setFont(font_symbol_box)

    def _QPushButton_properties(self):
        # -- QFont attributes for the QPushButton attributes --
        # To change QPushButton's attributes font
        font_button = QFont()
        font_symbol = QFont()

        # For the QLineEdit 'button_num(s)' attributes
        font_button.setPointSize(font_button.pointSize() + 6)
        font_button.setBold(True)
        # For the QLineEdit 'symbol(s)' attributes
        font_symbol.setPointSize(font_symbol.pointSize() + 10)
        # ---------------------------------------------------

        # ------------------------------------------------------------
        # Assigning our QFont attributes to our QPushButton attributes
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
        self.button_dot.setFont(font_symbol)
        # ------------------------------------------------------------

        # -----------------------------------------------------
        # Assigning a size policy to our QPushButton attributes
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
        #       * Symbol buttons
        self.button_backspace.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_clear_all.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_dot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_left_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_right_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # -----------------------------------------------------

    def _QGridLayout_properties(self):
        #           Regards the first row of the grid
        self.layout_grid.addWidget(self.display_box, 0, 1, 1, 3)
        self.layout_grid.addWidget(self.symbol_box, 0, 4, 1, 1)

        #       QPushButton attributes
        #           Regards the second row of the grid
        self.layout_grid.addWidget(self.button_clear_all, 1, 1)
        self.layout_grid.addWidget(self.button_backspace, 1, 2)
        self.layout_grid.addWidget(self.button_left_bracket, 1, 3)
        self.layout_grid.addWidget(self.button_right_bracket, 1, 4)

        #           Regards the third row of the grid
        self.layout_grid.addWidget(self.button_num7, 2, 1)
        self.layout_grid.addWidget(self.button_num8, 2, 2)
        self.layout_grid.addWidget(self.button_num9, 2, 3)
        self.layout_grid.addWidget(self.button_division, 2, 4)

        #           Regards the fourth row of the grid
        self.layout_grid.addWidget(self.button_num4, 3, 1)
        self.layout_grid.addWidget(self.button_num5, 3, 2)
        self.layout_grid.addWidget(self.button_num6, 3, 3)
        self.layout_grid.addWidget(self.button_times, 3, 4)

        #           Regards the fifth row of the grid
        self.layout_grid.addWidget(self.button_num1, 5, 1)
        self.layout_grid.addWidget(self.button_num2, 5, 2)
        self.layout_grid.addWidget(self.button_num3, 5, 3)
        self.layout_grid.addWidget(self.button_minus, 5, 4)

        #           Regards the sixth row of the grid
        self.layout_grid.addWidget(self.button_dot, 6, 1)
        self.layout_grid.addWidget(self.button_num0, 6, 2)
        self.layout_grid.addWidget(self.button_equal, 6, 3)
        self.layout_grid.addWidget(self.button_plus, 6, 4)

    def _QPushButton_signals(self):
        # ------------------------------------
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

        #       * Symbol button signals/events
        self.button_backspace.clicked.connect(self.pressed_button_backspace)
        self.button_clear_all.clicked.connect(self.pressed_button_clear_all)
        self.button_dot.clicked.connect(self.pressed_button_dot)
        # ------------------------------------

    def __init__(self):
        super().__init__()
        # -- QWidget's properties --
        self._QWidget_properties()  # Setting the widget's properties
        # --------------------------

        # ** DECLARATION & ALTERING OF ATTRIBUTES **
        # -- Boolean attributes --
        self.bool_waiting_for_operand = False
        # ------------------------

        # -- String attributes --
        self.string_display_box = ""
        self.string_symbol_box = ""
        # -----------------------

        # -- QLineEdit attributes --
        self.display_box = QLineEdit("")
        self.symbol_box = QLineEdit("")
        self._QLineEdit_properties()
        # --------------------------

        # -- QPushButton attributes --
        #       * Number buttons
        self.button_num1 = QPushButton("1")
        self.button_num2 = QPushButton("2")
        self.button_num3 = QPushButton("3")
        self.button_num4 = QPushButton("4")
        self.button_num5 = QPushButton("5")
        self.button_num6 = QPushButton("6")
        self.button_num7 = QPushButton("7")
        self.button_num8 = QPushButton("8")
        self.button_num9 = QPushButton("9")
        self.button_num0 = QPushButton("0")
        #       * Operand buttons
        self.button_equal = QPushButton("=")
        self.button_plus = QPushButton("+")
        self.button_minus = QPushButton("-")
        self.button_times = QPushButton("*")
        self.button_division = QPushButton("/")
        #       * Symbol buttons
        self.button_backspace = QPushButton("⌫")
        self.button_clear_all = QPushButton("CE")
        self.button_dot = QPushButton(".")
        self.button_left_bracket = QPushButton("(")
        self.button_right_bracket = QPushButton(")")
        self._QPushButton_properties()
        # ----------------------------

        # ** DECLARATION & ALTERING OF LAYOUT **
        # -- QGridLayout --
        self.layout_grid = QGridLayout()
        self._QGridLayout_properties()
        QWidget.setLayout(self, self.layout_grid)  # same as 'self.setLayout(self.layout_grid)'
        # -----------------

        # ** DECLARATION & ALTERING OF SIGNALS AND EVENTS **
        # -- QPushButton signals --
        self._QPushButton_signals()
        # -------------------------

    @Slot()
    # Slots & signals
    #       Number button signals
    def pressed_num0(self):
        # Displaying to the console, so we know the key has been pressed
        print("0 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "0")

    def pressed_num1(self):
        # Displaying to the console, so we know the key has been pressed
        print("1 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "1")

    def pressed_num2(self):
        # Displaying to the console, so we know the key has been pressed
        print("2 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "2")

    def pressed_num3(self):
        # Displaying to the console, so we know the key has been pressed
        print("3 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "3")

    def pressed_num4(self):
        # Displaying to the console, so we know the key has been pressed
        print("4 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "4")

    def pressed_num5(self):
        # Displaying to the console, so we know the key has been pressed
        print("5 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "5")

    def pressed_num6(self):
        # Displaying to the console, so we know the key has been pressed
        print("6 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "6")

    def pressed_num7(self):
        # Displaying to the console, so we know the key has been pressed
        print("7 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "7")

    def pressed_num8(self):
        # Displaying to the console, so we know the key has been pressed
        print("8 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "8")

    def pressed_num9(self):
        # Displaying to the console, so we know the key has been pressed
        print("9 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "9")

    # #       Operand buttons signals
    def pressed_button_equal(self):
        # Displaying to the console, so we know the key has been pressed
        print("= has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(str(sympy.sympify(self.display_box.text())))

    def pressed_button_plus(self):
        # Displaying to the console, so we know the key has been pressed
        print("+ has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "+")

    def pressed_button_minus(self):
        # Displaying to the console, so we know the key has been pressed
        print("- has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "-")

    def pressed_button_times(self):
        # Displaying to the console, so we know the key has been pressed
        print("* has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "*")

    def pressed_button_division(self):
        # Displaying to the console, so we know the key has been pressed
        print("/ has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "/")

    #       Symbol buttons signals
    def pressed_button_backspace(self):
        # Displaying to the console, so we know the key has been pressed
        print("⌫ has been pressed")
        # Calling the string_manipulator to handle the input/output
        st = self.display_box.text()
        st = st[:-1]
        self.display_box.setText(st)

    def pressed_button_clear_all(self):
        # Displaying to the console, so we know the key has been pressed
        print("CE has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.clear()

    def pressed_button_dot(self):
        # Displaying to the console, so we know the key has been pressed
        print(". has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + ".")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Calculator()
    widget.show()

    sys.exit(app.exec_())
