Mouse Movement Tracker and Analysis
This project tracks and analyzes mouse movements on your screen. The goal is to collect real-time mouse position data, visualize the paths, and generate insights like heatmaps to highlight areas of frequent interaction.

Features
Mouse Movement Tracking: Tracks the x and y coordinates of the mouse in real-time.
Data Logging: Logs mouse movements to a .txt file.
Data Visualization:
Curve Plot: Visualizes the mouse movement path.
Heatmap: Highlights areas of frequent mouse interaction.
User Interaction Insights: Useful for UX/UI design, user behavior analysis, and optimization of website/application layout.
Requirements
Python 3.x
pynput (for tracking mouse movements)
matplotlib (for plotting the data)
numpy (for data manipulation)
Installation
Clone the repository or download the project files.

Install Dependencies:

If you don’t have the required libraries installed, you can install them using pip:

bash
Copy code
pip install pynput matplotlib numpy
Usage
Track Mouse Movements:

Run the Python script to start tracking mouse movements. It will continuously log mouse positions to a .txt file.

Example command to start tracking:

bash
Copy code
python track_mouse.py
Data File:

The mouse positions are saved in mouse.txt in the format:

Copy code
x,y
100,200
150,250
300,400
You can analyze the data later using the visualization function.

Plotting the Data:

After collecting enough data, run the analysis script to generate a plot and heatmap.

bash
Copy code
python analyze_data.py
This will display a curve plot of the mouse path and a heatmap of frequently used areas.

Example Output
Curve Plot: A line graph showing the path of the mouse as it moves across the screen.
Heatmap: A visual representation highlighting areas of the screen with the most mouse interactions.
Use Cases
UX/UI Research: Study user interactions and focus areas on a webpage or app.
User Behavior Analysis: Identify how users navigate and interact with various elements on the screen.
Screen Usage Insights: Improve user experience by optimizing layout based on usage patterns.
Future Improvements
Track mouse clicks and interactions.
Provide real-time feedback on user behavior.
Integrate with web applications for live data collection.
