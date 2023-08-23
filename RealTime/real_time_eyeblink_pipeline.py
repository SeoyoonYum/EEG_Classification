from pylsl import StreamInlet, resolve_stream, StreamInfo
import numpy as np
import mne
import time
import socket

import serial_send as serial

# Headset Channel names
ch_names = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1','O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

# Headset sampling rate
sfreq = 128  # Hz

# Create the MNE Info object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)

def get_chunk():
    """
    returning chunk of 0.125s (14 channels)
    return numpy array data type
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
  
def realtime_blink_predict():
    """
    Real-time processing pipeline for eyeblink (main processing function)
    """
    data_reader = read_eeg()
    queue = []
    consecutive_blink_count = 0
    last_blink_time = None

    while True:

        eeg_data = next(data_reader)
        print(np.mean(eeg_data[0]))

        if np.mean(eeg_data[0]) > 4380:

            if 1 in queue:
                yield 0
                continue
            
            """
            
            current_time = time.time()
            if last_blink_time is None:
                last_blink_time = current_time
            else:
                time_interval = current_time - last_blink_time
                
                if time_interval <= 3 and time_interval >= 0.25:
                    consecutive_blink_count += 1
                else:
                    consecutive_blink_count = 0
            
                last_blink_time = current_time
            
            if consecutive_blink_count == 1:
                
                if len(queue) > 2:
                    queue.pop()
                queue.insert(0,1)
                yield 1
            
            elif consecutive_blink_count == 2:
                if len(queue) > 2:
                    queue.pop()
                queue.insert(0,2)
                yield 2

            elif consecutive_blink_count == 3:
                if len(queue) > 2:
                    queue.pop()
                queue.insert(0,3)

                yield 3
            else:
                if len(queue) > 2:
                    queue.pop()
                queue.insert(0,0)
            
                yield 0
            """
            if len(queue) > 2:
                    queue.pop()
            queue.insert(0,1)
            
            yield 1
            
        else:
            consecutive_blink_count = 0
            
            if len(queue) > 2:
                queue.pop()
            queue.insert(0, 0)
            
            yield 0
        

def send_gazebo(data):
    """
    Send prediction data to gazebo simulation
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
    TCP/IP protocol code for using simulation

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
    prediction = next(reader)

    while True:
        try:
            prediction = next(reader)
            if prediction == 0:
                print(prediction)
            else:
                count = 1
                for i in range(24):
                    prediction = next(reader)
                    if prediction == 1:
                        count += 1
                if count > 3:
                    count = 3
                print(count)
                #serial.send(count)
        except KeyboardInterrupt:
            serial.ser.close()
            
        
    #conn.close()  #connection closing for TCP/IP