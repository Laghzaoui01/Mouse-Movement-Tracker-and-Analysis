from pynput.mouse import Listener
import matplotlib.pyplot as plt
import numpy as np
import os

# Define the path to store the mouse movement data
file_path = r"C:\Users\SETUP GAME\Desktop\mouse.txt"  # Using raw string to avoid unicode escape error

# Set the screen resolution (adjust to your screen size)
screen_width = 1920
screen_height = 1080

# Create an empty 2D array to count mouse positions (heatmap)
mouse_grid = np.zeros((screen_height, screen_width))

# Function to log mouse data into the file
def log_mouse_data(x, y):
    with open(file_path, "a") as file:
        file.write(f"{x},{y}\n")
    
    if 0 <= x < screen_width and 0 <= y < screen_height:
        mouse_grid[y, x] += 1  # Increment the grid cell corresponding to the mouse position

# This function will be called whenever the mouse is moved
def on_move(x, y):
    log_mouse_data(x, y)

# This function will be called when a mouse button is pressed
def on_click(x, y, button, pressed):
    pass  # We're not using clicks in this case

# This function will be called when the mouse scrolls
def on_scroll(x, y, dx, dy):
    pass  # We're not using scroll in this case

# Start the listener for mouse movements
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

# Step 2: After stopping the listener, process the data and draw a curve

# Read the data from the file (mouse.txt)
x_coords = []
y_coords = []

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            x_coords.append(x)
            y_coords.append(y)

# Plot the mouse path as a curve
plt.figure(figsize=(10, 6))
plt.plot(x_coords, y_coords, label="Mouse Movement Path", color='blue', linewidth=1)
plt.title("Mouse Movement Path")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.legend()
plt.grid(True)
plt.show()

# Step 3: Draw a heatmap to analyze which areas are more used
plt.figure(figsize=(10, 6))
plt.imshow(mouse_grid, cmap='hot', interpolation='nearest')
plt.colorbar(label='Frequency of Mouse Movement')
plt.title("Mouse Activity Heatmap")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.show()

# Optionally, save the heatmap to a file
# plt.savefig("mouse_activity_heatmap.png")
