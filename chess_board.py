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

#Draw the chessboar
for row in range(board_size):
    for col in range(board_size):
        #Determine the color of the squares
        if (row + col) % 2 == 0:
            color = "white"
        else:
            color ="black"

        #Calculate the coordinates of the square
        x1 = col * square_size
        y1 = row * square_size

        x2 = x1 + square_size
        y2 = y1 + square_size

        #Draw the square
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# Run the Tkinter main loop
root.mainloop()