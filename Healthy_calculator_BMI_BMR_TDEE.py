from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from datetime import datetime
import matplotlib.pyplot as plt
import sqlite3

# Create SQLite
conn = sqlite3.connect('Health_data.db')
cur = conn.cursor()

cur.execute('''
Create TABLE IF NOT EXISTS Health_history(
date VARCHAR,
record_type VARCHAR,
record_value REAL,
PRIMARY KEY(date, record_type)
)
'''
)

conn.commit()
conn.close()


def cal_bmi():
    height_text = height_entry_bmi.get()
    weight_text = weight_entry_bmi.get()

    try:
        height = float(height_text)
        weight = float(weight_text)
        bmi = round(weight / (height / 100) ** 2, 1)
        comment = comparing_BMI(bmi)
        messagebox.showinfo(title = 'Result', message = f'Your BMI: {bmi} \n\n {comment}')
    except ValueError:
        messagebox.showerror(title = 'Error', message = 'Input error, please try again')


def cal_bmi_test(height, weight):
    return round(weight / (height / 100) ** 2, 1)

def save_bmi():
    height_text = height_entry_bmi.get()
    weight_text = weight_entry_bmi.get()
    current_date = datetime.now().date()
    current_date_str= str(current_date)

    try:
        height = float(height_text)
        weight = float(weight_text)
        bmi = round(weight / (height / 100) ** 2, 1)
    except ValueError:
        messagebox.showerror(title='Error', message='Input error, please try again')
        return

    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()

    cur.execute('INSERT OR REPLACE INTO Health_history (date, record_type, record_value) VALUES (?, ?, ?)',
                (current_date_str,'BMI', bmi))
    conn.commit()
    conn.close()
    messagebox.showinfo(title = "Save", message = 'Successfully')


def comparing_BMI(BMI):
    if BMI <18.5:
        return 'You are underweight'
    elif 18.5 <= BMI < 24:
        return 'You have healthy body weight'
    elif 24 <= BMI < 27:
        return 'You are overweight'
    elif 27<= BMI <30:
        return 'You are slight obesity'
    elif 30<= BMI <35:
        return 'You are middle obesity'
    else:
        return 'You are extreme obesity'


def cal_bmr_test(height,weight,sex,age):
    if sex == 'male':
        bmr = round(66 + (13.7 * weight + 5 * height - 6.8 * age), 2)
    elif sex == 'female':
        bmr = round(655 + (9.6 * weight + 1.8 * height - 4.7 * age), 2)
    return bmr


def cal_bmr():
    height_text = height_entry_bmr.get()
    weight_text = weight_entry_bmr.get()
    sex_text = sex_entry_bmr.get().lower()
    age_text = age_entry_bmr.get()
    try:
        height = float(height_text)
        weight = float(weight_text)
        age = float(age_text)
        if sex_text == 'male':
            bmr = round(66+(13.7 * weight + 5 * height - 6.8 * age), 2)
            messagebox.showinfo(title='Result', message=f'Your BMR: {bmr}')
        elif sex_text == 'female':
            bmr = round(655+(9.6 * weight + 1.8 * height - 4.7 * age), 2)
            messagebox.showinfo(title='Result', message=f'Your BMR: {bmr}')
        else:
            messagebox.showerror(title='Error', message='Please enter right sex')
    except ValueError:
        messagebox.showerror(title = 'Error', message = 'Input error, please try again')
    return



def save_bmr():
    height_text = height_entry_bmr.get()
    weight_text = weight_entry_bmr.get()
    sex_text = sex_entry_bmr.get().lower()
    age_text = age_entry_bmr.get()
    current_date = datetime.now().date()
    current_date_str= str(current_date)

    try:
        height = float(height_text)
        weight = float(weight_text)
        age = float(age_text)
        if sex_text == 'male':
            bmr = round(66 + (13.7 * weight + 5 * height - 6.8 * age), 2)
        elif sex_text == 'female':
            bmr = round(655 + (9.6 * weight + 1.8 * height - 4.7 * age), 2)
        else:
            messagebox.showerror(title='Error', message='Please enter right sex')
    except ValueError:
        messagebox.showerror(title='Error', message='Input error, please try again')
        return

    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()

    cur.execute('INSERT OR REPLACE INTO Health_history (date, record_type, record_value) VALUES (?,?,?)',
                (current_date_str, 'BMR', bmr))
    conn.commit()
    conn.close()
    messagebox.showinfo(title = "Save", message = 'Successfully')



def cal_tdee_test(height, weight, sex, age, activity_chose):
    activity_level_option = {
        "1 - Sedentary, little to no exercise": 1.2,
        "2 - Light exercise 1-3 days per week": 1.375,
        "3 - Moderate exercise 3-5 days per week": 1.55,
        "4 - Intense exercise 6-7 days per week": 1.725,
        "5 - Physically demanding job or intense daily training": 1.9
    }
    if sex == 'male':
        bmr = round(66 + (13.7 * weight + 5 * height - 6.8 * age), 2)
        tdee = round(bmr * activity_level_option[activity_chose], 2)
    elif sex == 'female':
        bmr = round(655 + (9.6 * weight + 1.8 * height - 4.7 * age), 2)
        tdee = round(bmr * activity_level_option[activity_chose], 2)
    return tdee




def cal_tdee():
    height_text = height_entry_tdee.get()
    weight_text = weight_entry_tdee.get()
    sex_text = sex_entry_tdee.get().lower()
    age_text = age_entry_tdee.get()
    activity_chose = activity_combobox.get()
    activity_level_option = {
        "1 - Sedentary, little to no exercise": 1.2,
        "2 - Light exercise 1-3 days per week": 1.375,
        "3 - Moderate exercise 3-5 days per week": 1.55,
        "4 - Intense exercise 6-7 days per week": 1.725,
        "5 - Physically demanding job or intense daily training": 1.9
    }
    try:
        height = float(height_text)
        weight = float(weight_text)
        age = float(age_text)
        if sex_text == 'male':
            bmr = round(66+(13.7 * weight + 5 * height - 6.8 * age), 2)
            tdee = round(bmr * activity_level_option[activity_chose], 2)
            messagebox.showinfo(title='Result', message=f'Your TDEE: {tdee}')
        elif sex_text == 'female':
            bmr = round(655+(9.6 * weight + 1.8 * height - 4.7 * age), 2)
            tdee = round(bmr * activity_level_option[activity_chose], 2)
            messagebox.showinfo(title='Result', message=f'Your TDEE: {tdee}')
        else:
            messagebox.showerror(title='Error', message='Please enter right sex')
    except ValueError:
        messagebox.showerror(title = 'Error', message = 'Input error, please try again')

def save_tdee():
    height_text = height_entry_tdee.get()
    weight_text = weight_entry_tdee.get()
    sex_text = sex_entry_tdee.get().lower()
    age_text = age_entry_tdee.get()
    activity_chose = activity_combobox.get()
    activity_level_option = {
        "1 - Sedentary, little to no exercise": 1.2,
        "2 - Light exercise 1-3 days per week": 1.375,
        "3 - Moderate exercise 3-5 days per week": 1.55,
        "4 - Intense exercise 6-7 days per week": 1.725,
        "5 - Physically demanding job or intense daily training": 1.9
    }
    try:
        height = float(height_text)
        weight = float(weight_text)
        age = float(age_text)
        current_date = datetime.now().date()
        current_date_str = str(current_date)
        if sex_text == 'male':
            bmr = round(66 + (13.7 * weight + 5 * height - 6.8 * age), 2)
            tdee = round(bmr * activity_level_option[activity_chose], 2)
        elif sex_text == 'female':
            bmr = round(655 + (9.6 * weight + 1.8 * height - 4.7 * age), 2)
            tdee = round(bmr * activity_level_option[activity_chose], 2)
        else:
            messagebox.showerror(title='Error', message='Please enter right sex')
    except ValueError:
        messagebox.showerror(title='Error', message='Input error, please try again')
        return

    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()
    cur.execute('INSERT OR REPLACE INTO Health_history (date, record_type, record_value) VALUES (?,?,?)',
                (current_date_str, 'TDEE', tdee))
    conn.commit()
    conn.close()
    messagebox.showinfo(title = "Save", message = 'Successfully')


def trace_bmi_history():
    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()
    cur.execute('SELECT date, record_type, record_value from Health_history where record_type = "BMI" ORDER BY date')
    records = cur.fetchall() # get all data like List
    conn.close()

    if records:
        dates = [record[0] for record in records]
        values = [record[2] for record in records]


        plt.figure(figsize=(10, 5))
        plt.plot(dates,values, marker='o', linestyle='-', color='r')
        plt.xlabel('Time')
        plt.ylabel('Your BMI')
        plt.title('BMI Trend')
        plt.xticks(rotation=45) # rotate label
        plt.tight_layout() # avoid overlap
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", "No BMI records found.")


def trace_bmr_history():
    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()
    cur.execute('SELECT date, record_type, record_value from Health_history where record_type = "BMR" ORDER BY date')
    records = cur.fetchall()
    conn.close()

    if records:
        dates = [record[0] for record in records]
        values = [record[2] for record in records]

        plt.figure(figsize=(10, 5))
        plt.plot(dates,values, marker='o', linestyle='-', color='r')
        plt.xlabel('Time')
        plt.ylabel('Your BMR')
        plt.title('BMR Trend')
        plt.xticks(rotation=45) # rotate label
        plt.tight_layout() # avoid overlap
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", "No BMR records found.")

def trace_tdee_history():
    conn = sqlite3.connect('Health_data.db')
    cur = conn.cursor()
    cur.execute('SELECT date, record_type, record_value from Health_history where record_type = "TDEE" ORDER BY date')
    records = cur.fetchall()
    conn.close()

    if records:
        date = [record[0] for record in records]
        value = [record[2] for record in records]

        plt.figure(figsize=(10,5))
        plt.plot(date, value, marker='o', linestyle='-', color='r')
        plt.xlabel('Time')
        plt.ylabel('Your TDEE')
        plt.title('TDEE Trend')
        plt.xticks(rotation = 45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", "No TDEE records found.")










if __name__ == '__main__':
    window = Tk()
    window.title('Welcome to the Comprehensive Health Calculator')
    window.geometry('500x500')
    window.resizable(False, False)
    # my_label = Label(text = 'test', font = ('Consolas',24), bg = 'green', fg = 'blue')
    # my_label.pack(side = 'top')
    window.config(padx = 40, pady = 5)

    # create different frame
    def show_frame(event):
        selected_option = option_combobox.get()
        frame_bmi.grid_forget()
        frame_bmr.grid_forget()
        frame_tdee.grid_forget()

        if selected_option == '1. Calculating Body Mass Index(BMI)':
            frame_bmi.grid(row=1, column=0)
        elif selected_option == "2. Calculating Basal Metabolic Rate(BMR)":
            frame_bmr.grid(row=1, column=0)
        else:
            frame_tdee.grid(row=1, column=0)




    # create option
    options = [
        "1. Calculating Body Mass Index(BMI)",
        "2. Calculating Basal Metabolic Rate(BMR)",
        "3. Calculating Total Daily Energy Expenditure(TDEE)"
    ]
    option_combobox = ttk.Combobox(window, width = 35, values = options)
    option_combobox.set('Please select the function you want')
    option_combobox.grid(row = 0, column = 0, padx = 20, pady = 50)
    option_combobox.bind("<<ComboboxSelected>>", show_frame)

    frame_bmi = tk.Frame(window)
    frame_bmr = tk.Frame(window)
    frame_tdee = tk.Frame(window)





    # create label and entry- BMI
    height_label = Label(frame_bmi, text = 'Height', font = ('Consolas', 23))
    height_label.grid(row = 0, column = 0, padx = 15, pady = 5)

    height_entry_bmi = Entry(frame_bmi, width = 15)
    height_entry_bmi.grid(row = 0, column = 1, padx = 15, pady = 5)

    cm_lable_bmi = Label(frame_bmi, text = 'cm')
    cm_lable_bmi.grid(row = 0, column = 2)

    weight_label = Label(frame_bmi, text = 'Weight', font = ('Consolas', 23))
    weight_label.grid(row = 1, column = 0, padx = 15, pady = 5)

    kg_label_bmi = Label(frame_bmi, text = 'kg')
    kg_label_bmi.grid(row = 1, column = 2)

    weight_entry_bmi = Entry(frame_bmi, width = 15)
    weight_entry_bmi.grid(row = 1, column = 1, padx = 15, pady = 5)

    cal_bmi_button = Button(frame_bmi, text = 'Calculate', command = cal_bmi)
    cal_bmi_button.grid(row = 2, column = 1)

    save_bmi_button = Button(frame_bmi, text = 'Save', command = save_bmi)
    save_bmi_button.grid(row = 3, column = 1)

    trace_bmi_button = Button(frame_bmi, text = 'History', command = trace_bmi_history)
    trace_bmi_button.grid(row = 4, column = 1)


    # create label and entry- BMR
    height_label = Label(frame_bmr, text = 'Height', font = ('Consolas', 23))
    height_label.grid(row = 0, column = 0, padx = 15, pady = 5)

    height_entry_bmr = Entry(frame_bmr, width = 15)
    height_entry_bmr.grid(row = 0, column = 1, padx = 15, pady = 5)

    weight_label = Label(frame_bmr, text = 'Weight', font = ('Consolas', 23))
    weight_label.grid(row = 1, column = 0, padx = 15, pady = 5)

    weight_entry_bmr = Entry(frame_bmr, width = 15)
    weight_entry_bmr.grid(row = 1, column = 1, padx = 15, pady = 5)
    sex_label = Label(frame_bmr, text = 'Sex', font = ('Consolas', 23))
    sex_label.grid(row = 3, column = 0, padx = 15, pady = 5)

    sex_entry_bmr = Entry(frame_bmr, width = 15)
    sex_entry_bmr.grid(row = 3, column = 1, padx = 15, pady = 5)

    age_label = Label(frame_bmr, text = 'Age', font = ('Consolas', 23))
    age_label.grid(row = 4, column = 0, padx = 15, pady = 5)

    age_entry_bmr = Entry(frame_bmr, width = 15)
    age_entry_bmr.grid(row = 4, column = 1, padx = 15, pady = 5)

    cal_bmr_button = Button(frame_bmr, text = 'Calculate', command = cal_bmr)
    cal_bmr_button.grid(row = 5, column = 1)

    save_bmr_button = Button(frame_bmr, text='Save', command=save_bmr)
    save_bmr_button.grid(row=6, column=1)

    trace_bmr_button = Button(frame_bmr, text = 'History', command = trace_bmr_history)
    trace_bmr_button.grid(row = 7, column = 1)

    # create label and entry- TDEE

    activity_level = [
        "1 - Sedentary, little to no exercise",
        "2 - Light exercise 1-3 days per week",
        "3 - Moderate exercise 3-5 days per week",
        "4 - Intense exercise 6-7 days per week",
        "5 - Physically demanding job or intense daily training"
    ]
    height_label = Label(frame_tdee, text = 'Height', font = ('Consolas', 23))
    height_label.grid(row = 1, column = 0, padx = 15, pady = 5)

    height_entry_tdee = Entry(frame_tdee, width = 15)
    height_entry_tdee.grid(row = 1, column = 1, padx = 15, pady = 5)

    weight_label = Label(frame_tdee, text = 'Weight', font = ('Consolas', 23))
    weight_label.grid(row = 2, column = 0, padx = 15, pady = 5)

    weight_entry_tdee = Entry(frame_tdee, width = 15)
    weight_entry_tdee.grid(row = 2, column = 1, padx = 15, pady = 5)

    sex_label = Label(frame_tdee, text = 'Sex', font = ('Consolas', 23))
    sex_label.grid(row = 3, column = 0, padx = 15, pady = 5)

    sex_entry_tdee = Entry(frame_tdee, width = 15)
    sex_entry_tdee.grid(row = 3, column = 1, padx = 15, pady = 5)

    age_label = Label(frame_tdee, text = 'Age', font = ('Consolas', 23))
    age_label.grid(row = 4, column = 0, padx = 15, pady = 5)

    age_entry_tdee = Entry(frame_tdee, width = 15)
    age_entry_tdee.grid(row = 4, column = 1, padx = 15, pady = 5)

    cal_tdee_button = Button(frame_tdee, text = 'Calculate', command = cal_tdee)
    cal_tdee_button.grid(row = 6, column = 1)

    save_tdee_button = Button(frame_tdee, text='Save', command=save_tdee)
    save_tdee_button.grid(row=7, column=1)

    trace_tdee_button = Button(frame_tdee, text = 'History', command = trace_tdee_history)
    trace_tdee_button.grid(row = 9, column = 1)

    # create Combobox
    activity_combobox = ttk.Combobox(frame_tdee, width = 33, values=activity_level)
    activity_combobox.set("Select activity level")  # show option title
    activity_combobox.grid(row = 5, column = 1, pady = 15)
    print(activity_combobox)

    window.mainloop()
