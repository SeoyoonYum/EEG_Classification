from pylsl import StreamInlet, resolve_stream, StreamInfo
import numpy as np
import mne
import time

"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""

import realtime_blink_preprocessing as pre
import realtime_blink_classification as cl

#import send_ros as send


# Example channel names
ch_names = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1','O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

# Example sampling rate
sfreq = 128  # Hz

# Create the MNE Info object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)

def get_chunk():
    """
    returning chunk of 0.125s (14 channels)
    """
    list = []
    for i in range(16):
        sample, timestamp = inlet.pull_sample()
        list.append(sample)
        
    eeg_data = np.array(list)
    eeg_data = eeg_data.T
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,14,0)
    eeg_data = np.delete(eeg_data,14,0)
    
    #print(f"Shape of chunk : {eeg_data.shape}")
    
    return eeg_data

def make_time_window():
    """
        Making the first time window of 0.5s
    """
    list = np.empty((14,0))
    for i in range(4):
        list = np.append(list, get_chunk(),axis = 1)
    
    #print(f"Time window shape : {list.shape}")
    #print(f"Window {list}")
    return list

def next_time_window(input_list):
    """
        Making the following time windows of 0.5s
    """
    list = input_list[:,16:]
    list = np.append(list, get_chunk(),axis = 1)
    #print(f"Next time window shape : {list.shape}")
    
    return list
"""
def plot_data(input):

    # Set the number of channels and samples
    num_channels = 14
    num_samples = 640

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

    def update_data(i):
        global data

        # Get new data for each channel
        new_data = input

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

"""
# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])


def read_eeg():
    """
    Reading a single eeg window (0.5S)
    """
    first_window = True
    
    while True:
        print("----------------------------------------------------------")
        
        if first_window:
            time_window = make_time_window()
            first_window = False
        else:
            time_window = next_time_window(time_window)
        #print(f"shape of window{time_window.shape}")
        
        print("----------------------------------------------------------")
        yield time_window
    
def realtime_predict():
    """
    Real-time processing pipeline (main function)
    """
    data_reader = read_eeg()
    while True:

        eeg_data = next(data_reader)

        
        # Convert the NumPy array to MNE Raw object
        eeg_data = mne.io.RawArray(eeg_data, info)
        

        # Preprocessing step
        preprocessed_data = preprocess(eeg_data)

        # Classifing step
        predicted_class = classify(preprocessed_data)
        print(predicted_class)
        yield predicted_class

def realtime_blink_predict():
    """
    Real-time processing pipeline (main function)
    """
    data_reader = read_eeg()
    queue = []
    

    while True:

        eeg_data = next(data_reader)
        print(np.mean(eeg_data[0]))
        #print(np.mean(eeg_data[13]))
        # Preprocessing step
        if np.mean(eeg_data[0]) > 4390 and 1 not in queue:
            
            queue.append(1)
            if len(queue) > 3:
                queue.pop()
            
            
            yield 1
        else:
            queue.append(0)
            if len(queue) > 3:
                queue.pop()
            
            
            yield 0
        

def preprocess(data):
    """
    data preprocessing function
    """
    pass
    return pre.preprocess(data)

def classify(data):
    """
    data classification function
    """
    pass
    #time.sleep(3)
    return cl.classification(data)

def send_data(data):
    """
    Send prediction data to arduino or simulation
    """
    pass
    #send.input_publisher(data)
    

if __name__ == "__main__":

    reader = realtime_blink_predict()
    check = 0
    while True:
        prediction = next(reader)
        print(prediction)
        if check != prediction and check == 0:
            print("Blink !!")
            send_data()
        check = prediction
            
        
