import tkinter as tk
import math
import datetime

# Function to calculate the interest
def calculate_interest():
    try:
        principal = float(principal_amount_entry.get())
        rate = float(rate_entry.get()) / 100
        years = int(years_entry.get())
        interest = principal * (rate * years)
        interest_label.config(text=f"Interest: {round(interest, 2)}")
    except ValueError:
        interest_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")

# Create a frame to hold the input fields and buttons
input_frame = tk.Frame(root)
input_frame.pack()

# Create a label for the principal amount
principal_amount_label = tk.Label(input_frame, text="Principal Amount:")
principal_amount_label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field to enter the principal amount
principal_amount_entry = tk.Entry(input_frame, width=10)
principal_amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label for the interest rate
rate_label = tk.Label(input_frame, text="Interest Rate:")
rate_label.grid(row=1, column=0, padx=10, pady=10)

# Create an entry field to enter the interest rate
rate_entry = tk.Entry(input_frame, width=10)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label for the number of years
years_label = tk.Label(input_frame, text="Number of Years:")
years_label.grid(row=2, column=0, padx=10, pady=10)

# Create an entry field to enter the number of years
years_entry = tk.Entry(input_frame, width=10)
years_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to calculate the interest
calculate_button = tk.Button(input_frame, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the interest
interest_label = tk.Label(input_frame, text="Interest:")
interest_label.grid(row=4, column=0, padx=10, pady=10)

# Run the main loop
root.mainloop()