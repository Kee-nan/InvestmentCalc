import tkinter as tk

# This program only uses a single function in order to gather all the variables and then calculate the result
def calculate():
    
    # Initializing variables and using .get with tkinter to pull the user's inputs
    principal = float(principal_entry.get())
    contributions = float(contributions_entry.get())
    years = float(years_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100  # Convert to decimal
    compounding_frequency = int(compounding_frequency_var.get()) 

    # Variable check for the frequency of the compounding
    if compounding_frequency == 12:
        n = 12  # Monthly compounding
    else:
        n = 1  # Annual compounding

    # Equation using the gathered variables to calculate the future value of the investment
    future_value = principal * (1 + (interest_rate / n))**(n * years) + contributions * ((1 + (interest_rate / n))**(n * years) - 1) / (interest_rate / n)

    # Display statement that will print the results of the calculation with a message in the tk GUI
    result_label.config(text=f"Your investment will grow to ${future_value:.2f} after {years} years")


# Tkinter GUI Components
root = tk.Tk()
root.title("Investment Calculator")

# Principal
principal_label = tk.Label(root, text="Principal:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

# Contributions
contributions_label = tk.Label(root, text="Additional Contributions:")
contributions_label.pack()
contributions_entry = tk.Entry(root)
contributions_entry.pack()

# Time
years_label = tk.Label(root, text="Time (Years):")
years_label.pack()
years_entry = tk.Entry(root)
years_entry.pack()

# Interest Rate
interest_rate_label = tk.Label(root, text="Annual Interest Rate (%):")
interest_rate_label.pack()
interest_rate_entry = tk.Entry(root)
interest_rate_entry.pack()

# Compounding frequency choice
compounding_frequency_label = tk.Label(root, text="Compounding Frequency:")
compounding_frequency_label.pack()
compounding_frequency_var = tk.IntVar()
compounding_frequency_var.set(12)  # Default to monthly compounding
monthly_radio = tk.Radiobutton(root, text="Monthly", variable=compounding_frequency_var, value=12)
annual_radio = tk.Radiobutton(root, text="Annually", variable=compounding_frequency_var, value=1)
monthly_radio.pack()
annual_radio.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()