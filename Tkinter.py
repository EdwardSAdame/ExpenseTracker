import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title and size of the window
root.title("My First Tkinter App")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)  # Add padding for better layout

# Run the application
root.mainloop()
