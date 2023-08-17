import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of channels and samples
num_channels = 14
num_samples = 640

data_range=(4000,4500)

# Create a figure and subplots for each channel
fig, axs = plt.subplots(num_channels, figsize=(12, 8), sharex=True, sharey=True)

# Create lines for each subplot
lines = [ax.plot(np.zeros(num_samples))[0] for ax in axs]

# Set plot labels and title
fig.suptitle('Real-Time EEG Data Plot')
fig.text(0.5, 0.04, 'Time (Samples)', ha='center')
fig.text(0.04, 0.5, 'EEG', va='center', rotation='vertical')

# Set the x-axis limit to maintain a fixed plot size
axs[0].set_xlim(0, num_samples)

# Adjust plot layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Initialize data for each channel
data = np.zeros((num_channels, num_samples))

def get_realtime_data():
    # Replace this function with your data acquisition logic
    # Generate random EEG data for demonstration
    return np.random.randint(data_range[0], data_range[1] + 1, size=(num_channels, 64))


def update_data(i):
    global data

    # Get new data for each channel
    new_data = get_realtime_data()

    # Shift the existing data to the left and append new data
    data[:, :-64] = data[:, 64:]
    data[:, -64:] = new_data

    # Update the y-data of each line in the subplots
    for line, y_data, ax in zip(lines, data, axs):
        line.set_ydata(y_data)
        ax.relim()
        ax.autoscale_view()

    return lines

# Create the animation
ani = animation.FuncAnimation(fig, update_data, interval=500)

# Display the plot
plt.show()

