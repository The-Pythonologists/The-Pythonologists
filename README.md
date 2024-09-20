# The-Pythonologists
No .exe file but the code is one .py file

Scripting a calculator with the bois ...  YES.

- Βασίλειος Κατωτομιχελάκης Π2020132
- Χαράλαμπος Μακρυλάκης Π2019214
- Αθανάσιος Καλαμάτας Π2020150
- Παναγιώτης Καράτζιας Π2020142

---

# Customisable Greek Calculator Application

This Python application is designed to provide a simple and user-friendly calculator in Greek. It supports both basic and complex calculations while offering a customizable user interface. The calculator is built using a graphical user interface (GUI), enhancing usability and accessibility for users.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Main Features](#main-features)
  - [Standard and Scientific Calculator](#standard-and-scientific-calculator)
  - [Body Mass Index (BMI) Calculator](#body-mass-index-bmi-calculator)
  - [Age Calculator](#age-calculator)
  - [Unit Conversions](#unit-conversions)
  - [Discount Calculator](#discount-calculator)
  - [UI Color Customization](#ui-color-customization)
- [Code Analysis](#code-analysis)
  - [Layout Setup](#layout-setup)
  - [Button Logic Handling](#button-logic-handling)
  - [Age Calculation Function](#age-calculation-function)

## Overview

Our goal was to create a Greek-language calculator that is not only easy to use but also provides support for both simple and complex calculations. To achieve this, we built the application using a **Graphical User Interface (GUI)** with Python.

## Tech Stack

- **Python**: Core programming language.
- **Qt for Python**: GUI framework used to design the layout with buttons, text fields, and a menu bar. It also allows customization of colors.
- **numexpr & math libraries**: Used for arithmetic calculations.
- **datetime module**: Used for age calculation.

## Main Features

### Standard and Scientific Calculator

The application provides two main modes:

- **Standard**  
  A basic calculator for simple arithmetic operations.

  ![image](https://github.com/user-attachments/assets/102afb8a-c681-4ace-a71b-cdfb5a27e0d0)
  
- **Scientific**  
  A scientific calculator that supports complex mathematical functions.

  ![image](https://github.com/user-attachments/assets/0a931c2b-1731-44d8-af10-93ac8c310eeb)

### UI of all the Modes

- **Modes List**

![image](https://github.com/user-attachments/assets/34163b41-3a6b-451d-991f-a0663fbb54db)

### Body Mass Index (BMI) Calculator

This feature allows users to calculate their BMI based on their weight and height, providing insights into their physical health.

![image](https://github.com/user-attachments/assets/b3414fd8-c063-43da-aa46-5ba91bc7df92)

### Age Calculator

The age calculator lets users compute their exact age in years, months, and days based on their input.

![image](https://github.com/user-attachments/assets/8d1da2b0-55b0-4f31-a383-c99caf8c8d9e)

### Unit Conversions

Various unit conversion options are available, such as converting between **MegaBytes (MB)** and **TeraBytes (TB)**.  

![image](https://github.com/user-attachments/assets/fd509d3e-4361-454b-9f1d-cee288d596ee)

### Discount Calculator

This feature allows users to calculate the final price after a discount is applied by entering the discount percentage and the original price.

![image](https://github.com/user-attachments/assets/bbd6bb2a-7644-46c7-9be1-1cacf3589349)

### UI Color Customization

The user can modify the application's theme and colors, making the interface more personalized and visually appealing.  

![image](https://github.com/user-attachments/assets/086fa940-b041-4255-be07-95a127f78dc3)

## Code Analysis

### Layout Setup

The code arranges the Qt objects (buttons, text fields, etc.) within the layout, ensuring they appear correctly in the application window.

### Button Logic Handling

Each arithmetic button corresponds to a number, and when pressed, it displays the appropriate number in the display box. This logic is handled using separate functions and boolean variables that manage the button interactions.

### Example of Age Calculation Function

The `calculate_age` function takes the user's input in the form of **day/month/year** (D/M/Y), performs the necessary calculations, and converts the result into a string, which is then displayed in the `symbol_box_age`.
