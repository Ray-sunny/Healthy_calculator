# Health Calculator

The Health Calculator is a Python-based application designed to provide users with essential health metrics including BMI (Body Mass Index), BMR (Basal Metabolic Rate), and TDEE (Total Daily Energy Expenditure). 
This project features a GUI built with Tkinter, stores data using SQLite, and provides graphical visualization of historical data with Matplotlib.

## Key Features

- **BMI Calculation**: Computes BMI based on user input for height and weight and provides feedback on health status.
- **BMR Calculation**: Determines Basal Metabolic Rate based on height, weight, gender, and age.
- **TDEE Calculation**: Calculates Total Daily Energy Expenditure using BMR results and the user's selected activity level.
- **Data Persistence**: Utilizes an SQLite database for saving and retrieving health data records, ensuring persistence between sessions.
- **Historical Data Visualization**: Uses Matplotlib to graphically display trends in BMI, BMR, and TDEE over time.

## Tech Stack

- **Python 3**: A core programming language for the project.
- **Tkinter**: Provides the graphical user interface.
- **SQLite**: Database system used for storing and managing health records.
- **Matplotlib**: Generates trend graphs for BMI, BMR, and TDEE.
- **Unittest**: Comprehensive unit tests ensure the reliability of BMI, BMR, and TDEE calculations.

## Project Structure

```plaintext
Health_calculator/
├── main.py               # Main application script
├── database/             # Database folder
│   └── Health_data.db    # SQLite database file
├── tests/                # Unit tests folder
│   ├── test_bmi.py       # Unit tests for BMI calculation
│   ├── test_bmr.py       # Unit tests for BMR calculation
│   └── test_tdee.py      # Unit tests for TDEE calculation
└── README.md             # Project documentation

Installation & Usage
Requirements
Python 3.x
Matplotlib
Installation
