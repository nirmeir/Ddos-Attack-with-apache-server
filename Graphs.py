import matplotlib.pyplot as plt
import numpy as np

# Open the file in read-only mode
with open("pings_results_p.txt", "r") as file:
    # Read the contents of the file into a list of strings
    py_ping_data = file.readlines()
    print(py_ping_data)

# RTT
i = 1
# Define a list of x values
x_values = []
# Get the length of the py_ping_data list
data_length = len(py_ping_data)

# Iterate over the list until we reach the end of the list
while i < data_length and len(x_values) < 100:
    # Split the string and extract the numeric value
    line_i = py_ping_data[i].split(' ')
    x = float(line_i[1]) * 1000  # convert sec to milisec
    # Add the value to the x_values list
    x_values.append(x)
    # Increment the index
    i += 2

# number of pings
j = 0
# Define a list of y values
y_values = []

# Iterate over the list until we reach the end of the list
while j < data_length-1 and len(y_values) < 100:
    # Split the string and extract the numeric value
    line_j = py_ping_data[j].split(' ')
    y = int(line_j[1])
    # Add the value to the y_values list
    y_values.append(y)
    # Increment the index
    j += 2

print(x_values)
print(y_values)

# x_values and y_values are the lists of x- and
# y-coordinates for the points on the graph.
plt.plot(x_values, y_values)

# Get the Axes object returned by the plot method
axes = plt.gca()

# Use the Axes object to set the labels and title
axes.set_xlabel('RTT values')
axes.set_ylabel('ping number')
axes.set_title('Pings Python')

plt.show()

plt.savefig("Pings_p.png")





