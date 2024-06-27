# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:23:25 2024

@author: shiva
"""

import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    pincode = pincode_entry.get()
    state = state_entry.get()
    country = country_entry.get()
    gender = gender_var.get()
    
    # Perform validation
    if not name or not email or not age or not phone or not address or not city or not pincode or not state or not country or not gender:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    # Further validation logic can be added here
    
    # Registration successful
    messagebox.showinfo("Success", "Registration successful!\nName: {}\nEmail: {}\nAge: {}\nPhone: {}\nAddress: {}\nCity: {}\nPincode: {}\nState: {}\nCountry: {}\nGender: {}".format(name, email, age, phone, address, city, pincode, state, country, gender))
    
    # Clear the entry fields after registration
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    pincode_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    gender_male.deselect()
    gender_female.deselect()

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

city_label = tk.Label(root, text="City:")
city_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
city_entry = tk.Entry(root)
city_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

pincode_label = tk.Label(root, text="Pincode:")
pincode_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
pincode_entry = tk.Entry(root)
pincode_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

state_label = tk.Label(root, text="State:")
state_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
state_entry = tk.Entry(root)
state_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

country_label = tk.Label(root, text="Country:")
country_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
country_entry = tk.Entry(root)
country_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")

gender_var = tk.StringVar(root)
gender_var.set("Male")
gender_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male.grid(row=9, column=1, padx=10, pady=5, sticky="w")

gender_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female.grid(row=10, column=1, padx=10, pady=5, sticky="w")

# Center the window
window_width = 400
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Create submit button
submit_button = tk.Button(root, text="Register", command=register)
submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
