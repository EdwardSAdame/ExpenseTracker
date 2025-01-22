import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

# Global list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    description = desc_entry.get()
    amount = amount_entry.get()

    # Validate inputs
    if not description or not amount:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return
    
    # Add to expenses list
    expenses.append((description, amount))
    update_expense_list()
    clear_inputs()

# Function to clear the input fields
def clear_inputs():
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Function to update the expense list display
def update_expense_list():
    total = sum(expense[1] for expense in expenses)
    expense_list.delete(0, tk.END)  # Clear the current list
    for i, (desc, amt) in enumerate(expenses, start=1):
        expense_list.insert(tk.END, f"{i}. {desc}: ${amt:.2f}")
    total_label.config(text=f"Total: ${total:.2f}")

# GUI Layout

# Description field
desc_label = tk.Label(root, text="Description:")
desc_label.pack(pady=5)
desc_entry = tk.Entry(root, width=30)
desc_entry.pack(pady=5)

# Amount field
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

# Add button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack(pady=10)

# Expense list display
expense_list = tk.Listbox(root, width=50)
expense_list.pack(pady=10)

# Total display
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14))
total_label.pack(pady=10)

# Run the application
root.mainloop()
