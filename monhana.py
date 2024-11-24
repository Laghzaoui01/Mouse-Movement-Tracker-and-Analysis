import matplotlib.pyplot as plt

# Function to read data from the file and return x and y coordinates
def read_data(file_path):
    x_coords = []
    y_coords = []
    
    # Read the file and parse the x, y values
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line by the comma and convert to integers
                x, y = map(int, line.strip().split(','))
                x_coords.append(x)
                y_coords.append(y)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    
    return x_coords, y_coords

# Function to plot the data as a curve
def plot_curve(x_coords, y_coords):
    plt.figure(figsize=(10, 6))
    plt.plot(x_coords, y_coords, label="Data Curve", color='blue', linewidth=2)
    plt.title("Curve of Data Points")
    plt.xlabel("X Coordinates")
    plt.ylabel("Y Coordinates")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to execute the script
if __name__ == "__main__":
    file_path = r'C:\Users\SETUP GAME\Desktop\mouse.txt'  # Using raw string here
    x_coords, y_coords = read_data(file_path)
    
    if x_coords and y_coords:
        plot_curve(x_coords, y_coords)
    else:
        print("No data to plot.")
