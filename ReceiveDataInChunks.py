"""Example program to demonstrate how to read a multi-channel time-series
from LSL in a chunk-by-chunk manner (which is more efficient)."""

from pylsl import StreamInlet, resolve_stream, StreamInfo
import numpy as np
import mne

# Example channel names
ch_names = ['AF3', 'F7', 'F3', 'FC5', '2T7', 'P7', 'O1','O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

# Example sampling rate
sfreq = 128  # Hz

# Example montage (set to None if not available)
montage = None

# Create the MNE Info object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)


# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

print(StreamInfo().name())
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    chunk, timestamps = inlet.pull_chunk(0.125)
    
    
    
    if len(chunk)  == 0:
        continue
    elif len(chunk) != 16:
        continue

    eeg_data = np.array(chunk)
    eeg_data = eeg_data.T
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,0,0)
    eeg_data = np.delete(eeg_data,14,0)
    eeg_data = np.delete(eeg_data,14,0)
    print(eeg_data.shape)
    # Convert the NumPy array to MNE Raw object
    #raw = mne.io.RawArray(eeg_data.T, info)
    #print(raw)
    #raw.save(fname = "raw.fif", overwrite = True, split_naming='neuromag')






