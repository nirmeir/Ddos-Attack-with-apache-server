import matplotlib.pyplot as plt


def syns_graph(filename):
    # Open the file in read-only mode
    with open(filename, "r") as file:
        # Read the contents of the file into a list of strings
        syns_data = file.readlines()
        print(syns_data)

    # time
    i = 1
    # Define a list of x values
    x_values = []
    # Get the length of the syns_data list
    data_length = len(syns_data)

    # Iterate over the list until we reach 100 values
    while i < data_length and len(x_values) < 100:
        # Split the string and extract the numeric value
        line_i = syns_data[i].split(' ')
        x = float(line_i[3]) * 1000  # convert sec to milisec
        # Add the value to the x_values list
        x_values.append(x)
        # Increment the index
        i += 2

    # number of packet
    j = 0
    # Define a list of y values
    y_values = []

    # Iterate over the list until we reach 100 values
    while j < data_length-1 and len(y_values) < 100:
        # Split the string and extract the numeric value
        line_j = syns_data[j].split(' ')
        y = int(line_j[4])
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
    axes.set_xlabel('Time to send a packet')
    axes.set_ylabel('number of packets sent')
    axes.set_title('Syns Python')

    plt.show()


def pings_graph(filename):
    # Open the file in read-only mode
    with open(filename, "r") as file:
        # Read the contents of the file into a list of strings
        ping_data = file.readlines()
        print(ping_data)

    # RTT
    i = 1
    # Define a list of x values
    x_values = []
    # Get the length of the ping_data list
    data_length = len(ping_data)

    # Iterate over the list until we reach 100 values
    while i < data_length and len(x_values) < 100:
        # Split the string and extract the numeric value
        line_i = ping_data[i].split(' ')
        x = float(line_i[1]) * 1000  # convert sec to milisec
        # Add the value to the x_values list
        x_values.append(x)
        # Increment the index
        i += 2

    # number of pings
    j = 0
    # Define a list of y values
    y_values = []

    # Iterate over the list until we reach 100 values
    while j < data_length-1 and len(y_values) < 100:
        # Split the string and extract the numeric value
        line_j = ping_data[j].split(' ')
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


if __name__ == '__main__':
    #pings_graph("pings_results_p.txt")
    syns_graph("syns_results_p.txt")


