import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Chess Board")

# Set the dimensions of the chessboard
board_size = 8 #Number of squares per row/column
square_size = 50 #Size of each square in pixels
canvas_size = board_size*square_size

#Create a canvas widget
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()


# Run the Tkinter main loop
root.mainloop()
