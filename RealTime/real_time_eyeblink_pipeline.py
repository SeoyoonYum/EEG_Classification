from pylsl import StreamInlet, resolve_stream, StreamInfo
import numpy as np
import mne
import time
import socket
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""

import realtime_blink_preprocessing as pre
import realtime_blink_classification as cl

import serial_send as serial

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

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
for stream in streams:
    print(stream.name())
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
    consecutive_blink_count = 0
    last_blink_time = None

    while True:

        eeg_data = next(data_reader)
        print(np.mean(eeg_data[0]))
        #print(np.mean(eeg_data[13]))

        if np.mean(eeg_data[0]) > 4390 and 1 not in queue:
            current_time = time.time()
            if last_blink_time is None:
                last_blink_time = current_time
            else:
                time_interval = current_time - last_blink_time
                
                if time_interval <= 2:
                    consecutive_blink_count += 1
                else:
                    consecutive_blink_count = 0
            
            last_blink_time = current_time
            
            if consecutive_blink_count == 2:
                queue.append(1)
                if len(queue) > 2:
                    queue.pop()
                yield 1
            
            if consecutive_blink_count == 3:
                queue.append(2)
                if len(queue) > 2:
                    queue.pop()
                yield 2

            if consecutive_blink_count == 4:
                queue.append(3)
                if len(queue) > 2:
                    queue.pop()
                yield 3
        else:
            consecutive_blink_count = 0
            queue.append(0)
            if len(queue) > 2:
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
    Send prediction data to simulation
    """
    

    
    if data == 1:
        send = "o"
        conn.sendall(send.encode())
    else:
        send = "p"
        conn.sendall(send.encode())


    #send.input_publisher(data)
    

if __name__ == "__main__":
    
    """
    
    host = '0.0.0.0' # Listen on all available interfaces
    port = 12345     # Use port 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Listening on {host}:{port}")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    """

    reader = realtime_blink_predict()
    
    while True:
        try:
            prediction = next(reader)
            print(prediction)
            serial.send(prediction)
        except KeyboardInterrupt:
            serial.ser.close()
            
        
    #conn.close()