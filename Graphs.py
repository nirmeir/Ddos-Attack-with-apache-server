import matplotlib.pyplot as plt


def syns_graph(filename):
    # Open the file in read-only mode
    with open(filename, "r") as file:
        # Read the contents of the file into a list of strings
        syns_data = file.readlines()

    # time of sending a packet
    i = 1
    # number of packet
    j = 0
    # Define a list of x values
    x_values = []
    # Define a list of y values
    y_values = []
    # Get the length of the syns_data list
    data_length = len(syns_data)

    x = 0
    y = 0  # number of packets in a scope of time
    timeLimitCounter = 0

    # Iterate over the list until we reach the end of the data
    while i < data_length and j < data_length-1:

        while timeLimitCounter < 15:
            # Split the string and extract the numeric value
            line_i = syns_data[i].split(' ')
            line_j = syns_data[j].split(' ')

            thisPacketTime = float(line_i[3]) * 1000  # convert sec to milisec
            thisPacketIndex = int(line_j[4])

            x += thisPacketTime
            timeLimitCounter += thisPacketTime
            y += 1  # increment the number of packets in this time scope

            j += 2  # Increment the index
            i += 2

        # Add the value to the x_values list
        x_values.append(x)
        # Add the value to the y_values list
        y_values.append(y)

        timeLimitCounter = 0
        y = 0

    print(x_values)
    print(y_values)

    # x_values and y_values are the lists of x- and
    # y-coordinates for the points on the graph.
    plt.bar(x_values, y_values, color = "red")

    # Get the Axes object returned by the plot method
    axes = plt.gca()

    # Use the Axes object to set the labels and title
    axes.set_xlabel('Time sending in milisec')
    axes.set_ylabel('packets sent every 15 milisec')
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
    # number of pings
    j = 0
    # Define a list of y values
    y_values = []


    # Iterate over the list
    while i < data_length and j < data_length-1:

        # Split the string and extract the numeric value
        line_i = ping_data[i].split(' ')
        line_j = ping_data[j].split(' ')
        y = float(line_i[1]) * 1000  # convert sec to milisec
        x = int(line_j[1])

        # Increment the index
        i += 2
        j += 2

        x_values.append(x)  # the ping id number
        y_values.append(y)  # the rtt value



    print(x_values)
    print(y_values)

    # x_values and y_values are the lists of x- and
    # y-coordinates for the points on the graph.
    plt.bar(x_values, y_values, color = "red")

    # Get the Axes object returned by the plot method
    axes = plt.gca()

    # Use the Axes object to set the labels and title
    axes.set_xlabel('packet id')
    axes.set_ylabel('rtt for each packet')
    axes.set_title('Pings Python')

    plt.show()


if __name__ == '__main__':
    pings_graph("pings_results_p.txt")
    #syns_graph("syns_results_p.txt")


