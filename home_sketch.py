import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Sketch of a Home")
root.geometry("400x400")

# Create a Canvas widget for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="skyblue")
canvas.pack()

# Draw the base of the house (rectangle)
canvas.create_rectangle(100, 200, 300, 350, fill="burlywood", outline="black")

# Draw the roof of the house (triangle)
canvas.create_polygon(100, 200, 300, 200, 200, 100, fill="brown", outline="black")

# Draw the door (rectangle)
canvas.create_rectangle(180, 270, 220, 350, fill="saddlebrown", outline="black")

# Draw windows (rectangles)
canvas.create_rectangle(120, 220, 160, 260, fill="white", outline="black")  # Left window
canvas.create_rectangle(240, 220, 280, 260, fill="white", outline="black")  # Right window

# Draw the sun (circle)
canvas.create_oval(320, 50, 370, 100, fill="yellow", outline="orange")

# Draw some grass (lines)
for x in range(0, 400, 10):
    canvas.create_line(x, 350, x + 5, 370, fill="green")

# Add some text
canvas.create_text(200, 370, text="My Home Sketch", font=("Arial", 14, "bold"), fill="black")

# Run the Tkinter main loop
root.mainloop()
